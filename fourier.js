function dft(x) {
    const N = x.length;
    const X = [];
    for (let k = 0; k < N; k++) {
      let real = 0;
      let im = 0;
      for (let n = 0; n < N; n++) {
        const phi = (TWO_PI * k * n) / N;
        real += x[n] * cos(phi);
        im -= x[n] * sin(phi);
      }
      real = real / N;
      im = im / N;
  
      let freq = k;
      let amplitude = sqrt(real * real + im * im);
      let phase = atan2(im, real);
      X[k] = { real, im, freq, amplitude, phase };
    }
    return X;
  }