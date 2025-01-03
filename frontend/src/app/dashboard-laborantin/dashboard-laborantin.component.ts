import { Component, ChangeDetectorRef } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Chart } from 'chart.js/auto';

interface Bilan {
  name: string;
  value: string | null;
  unity: string | null;
}

interface Test {
  id: number;
  date: string;
  bilans: Bilan[];
  status: 'Completed' | 'Pending';
  compteRendu: string;
  graphData: any | null;
}

@Component({
  selector: 'app-dashboard-laborantin',
  templateUrl: './dashboard-laborantin.component.html',
  styleUrls: ['./dashboard-laborantin.component.css'],
  standalone: true,
  imports: [CommonModule, FormsModule],
})
export class DashboardLaborantinComponent {
  private chart: Chart | null = null;
  
  showDialog = false;
  selectedTest: Test | null = null;
  generateGraph = false;

  tests: Test[] = [
    {
      id: 1,
      date: '2023-10-01',
      bilans: [
        { name: 'b1', value: '120', unity: 'mg/dL' },
        { name: 'b2', value: '5.5', unity: 'mmol/L' },
      ],
      status: 'Completed',
      compteRendu: 'All results are within normal range.',
      graphData: null
    },
    {
      id: 2,
      date: '2023-10-02',
      bilans: [
        { name: 'b1', value: null, unity: null },
        { name: 'b2', value: null, unity: null },
      ],
      status: 'Pending',
      compteRendu: '',
      graphData: null
    }
  ];

  constructor(private router: Router, private cdr: ChangeDetectorRef) {}

  navigateToProfile() {
    this.router.navigate(['/profile']);
  }

  openDialog(test: Test) {
    this.selectedTest = JSON.parse(JSON.stringify(test));
    this.generateGraph = false;
    this.showDialog = true;
    
    if (test.status === 'Completed') {
      this.generateGraph = true;
      setTimeout(() => {
        this.createOrUpdateChart();
      }, 100);
    }
  }

  closeDialog() {
    if (this.chart) {
      this.chart.destroy();
      this.chart = null;
    }
    this.showDialog = false;
    this.selectedTest = null;
    this.generateGraph = false;
  }

  createOrUpdateChart() {
    if (!this.selectedTest) return;

    const validBilans = this.selectedTest.bilans.filter(b => b.value !== null && b.value !== '');
    if (validBilans.length === 0) return;

    const canvas = document.getElementById('bilanChart') as HTMLCanvasElement;
    if (!canvas) return;

    // If chart exists, destroy it first
    if (this.chart) {
      this.chart.destroy();
    }

    // Create new chart
    this.chart = new Chart(canvas, {
      type: 'bar',
      data: {
        labels: validBilans.map(b => b.name),
        datasets: [{
          label: 'Test Results',
          data: validBilans.map(b => parseFloat(b.value || '0')),
          backgroundColor: validBilans.map((_, i) => 
            i % 2 === 0 ? '#36A2EB' : '#FF6384'
          ),
          borderColor: validBilans.map((_, i) => 
            i % 2 === 0 ? '#36A2EB' : '#FF6384'
          ),
          borderWidth: 1
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  }

  onBilanValueChange() {
    if (this.generateGraph) {
      this.createOrUpdateChart();
    }
  }

  updateStatus() {
    if (!this.selectedTest) return;

    const isValid = this.selectedTest.bilans.every(b => 
      b.value !== null && b.value !== '' && b.unity !== null && b.unity !== ''
    );

    if (!isValid) {
      alert('Please fill in all bilan values and units');
      return;
    }

    const originalTest = this.tests.find(t => t.id === this.selectedTest?.id);
    if (originalTest && this.selectedTest) {
      Object.assign(originalTest, this.selectedTest);
      originalTest.status = 'Completed';
    }

    this.cdr.detectChanges();
    this.closeDialog();
  }
}