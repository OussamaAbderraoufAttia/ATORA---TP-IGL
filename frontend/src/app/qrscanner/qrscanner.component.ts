import { Component, OnInit } from '@angular/core';
import { BrowserMultiFormatOneDReader, BrowserMultiFormatReader } from '@zxing/browser';
import { Result } from '@zxing/library';
import{ CommonModule } from '@angular/common';


@Component({
  selector: 'app-qrscanner',
  imports: [ CommonModule],
  templateUrl: './qrscanner.component.html',
  styleUrl: './qrscanner.component.css'
})
export class QrscannerComponent implements OnInit{
  result: string | null = null;

  private codeReader: BrowserMultiFormatReader;
   isScanneron = false;

  constructor() {
    this.codeReader = new BrowserMultiFormatReader();
  }

  ngOnInit(): void {
    this.startScanner();
  }

  async startScanner(): Promise<void> {
    try {
      this.isScanneron = true;
      const videoInputDevices = await BrowserMultiFormatReader.listVideoInputDevices();
      if (videoInputDevices.length === 0) {
        alert('No camera found!');
        return;
      }

      // Select the first available video device
      const selectedDeviceId = videoInputDevices[0].deviceId;

      this.codeReader.decodeFromVideoDevice(selectedDeviceId, 'video', (result, error) => {
        if (result) {
          this.result = result.getText();
          console.log('QR Code result:', this.result);
        }
      });
    } catch (err) {
      console.error('Error during scanning:', err);
    }
  }
  stopScanner(): void {
    BrowserMultiFormatOneDReader.releaseAllStreams();
    this.isScanneron = false;
  }
}
