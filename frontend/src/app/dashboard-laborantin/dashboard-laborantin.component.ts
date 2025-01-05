import { Component, ChangeDetectorRef } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Chart } from 'chart.js/auto';

interface Mesure {
  param: string;
  valeur: string;
}

interface BilanBiologique {
  id_bilanbiologique: number;
  consultation: number;
  description: string;
  date: string;
  status: 'done' | 'requested';
  mesures: Mesure[];
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
  selectedBilan: BilanBiologique | null = null;
  generateGraph = false;

  bilans: BilanBiologique[] = [
    {
      id_bilanbiologique: 1,
      consultation: 1,
      description: "updated one",
      date: "2025-01-05",
      status: "done",
      mesures: [
        {  param: "param1", valeur: "0.98" },
        {  param: "param2", valeur: "value2" }
      ]
    },
    {
      id_bilanbiologique: 2,
      consultation: 2,
      description: "Normal blood count",
      date: "2025-01-04",
      status: "requested",
      mesures: []
    },
    {
      id_bilanbiologique: 3,
      consultation: 3,
      description: "Normal blood count",
      date: "2025-01-04",
      status: "requested",
      mesures: []
    },
    {
      id_bilanbiologique: 4,
      consultation: 4,
      description: "Normal blood count",
      date: "2025-01-04",
      status: "requested",
      mesures: []
    }
  ];

  constructor(private router: Router, private cdr: ChangeDetectorRef) {}

  navigateToProfile() {
    this.router.navigate(['/profile']);
  }

  openDialog(bilan: BilanBiologique) {
    this.selectedBilan = JSON.parse(JSON.stringify(bilan));
    this.generateGraph = false;
    this.showDialog = true;

    if (bilan.status === 'done') {
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
    this.selectedBilan = null;
    this.generateGraph = false;
  }

  createOrUpdateChart() {
    if (!this.selectedBilan) return;

    const validMesures = this.selectedBilan.mesures.filter(m => m.valeur);
    if (validMesures.length === 0) return;

    const canvas = document.getElementById('bilanChart') as HTMLCanvasElement;
    if (!canvas) return;

    if (this.chart) {
      this.chart.destroy();
    }

    this.chart = new Chart(canvas, {
      type: 'bar',
      data: {
        labels: validMesures.map(m => m.param),
        datasets: [{
          label: `${this.selectedBilan.description} Results`,
          data: validMesures.map(m => parseFloat(m.valeur)),
          backgroundColor: validMesures.map((_, i) =>
            i % 2 === 0 ? '#36A2EB' : '#FF6384'
          ),
          borderColor: validMesures.map((_, i) =>
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

  onMesureValueChange() {
    if (this.generateGraph) {
      this.createOrUpdateChart();
    }
  }

  addMesure() {
    if (this.selectedBilan) {
      this.selectedBilan.mesures.push({ param: '', valeur: '' }); // `id_mesure` is temporary
    }
  }

  removeMesure(index: number) {
    if (this.selectedBilan) {
      this.selectedBilan.mesures.splice(index, 1);
    }
  }

  prepareBackendObject(): { mesures: Mesure[] } {
    if (!this.selectedBilan) return { mesures: [] };

    return {
      mesures: this.selectedBilan.mesures.filter(m => m.param && m.valeur) // Filter out empty values
    };
  }

  updateStatus() {
    if (!this.selectedBilan) return;

    const isValid = this.selectedBilan.mesures.every(m => m.param && m.valeur);
    if (!isValid) {
      alert('Please fill in all parameter names and values');
      return;
    }

    const backendObject = this.prepareBackendObject();
    console.log('Object to send to the backend:', backendObject);

    const originalBilan = this.bilans.find(b => b.id_bilanbiologique === this.selectedBilan?.id_bilanbiologique);
    if (originalBilan && this.selectedBilan) {
      Object.assign(originalBilan, this.selectedBilan);
      originalBilan.status = 'done';
    }

    this.cdr.detectChanges();
    this.closeDialog();
  }
}