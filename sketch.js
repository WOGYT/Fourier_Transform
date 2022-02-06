// Coding Challenge 130.1: Drawing with Fourier Transform and Epicycles
// Daniel Shiffman
// Copyright (c) 2019 Coding Train
// https://thecodingtrain.com/CodingChallenges/130-fourier-transform-drawing.html
// https://youtu.be/MY4luNgGfms
// https://editor.p5js.org/codingtrain/sketches/jawHqwfda

let x = [];
let y = [];
let fourierX;
let fourierY;
let time = 0;
let path = [];

height_window = window.innerWidth
width_window = window.innerHeight

function setup() {
  createCanvas(height_window, width_window);
  const skip = 15;
  for (let i = 0; i < drawing_2.length; i += skip) {
    x.push(drawing_2[i].x);
    y.push(drawing_2[i].y);
  }
  fourierX = dft(x);
  fourierY = dft(y);

  fourierX.sort((a, b) => b.amplitude - a.amplitude);
  fourierY.sort((a, b) => b.amplitude - a.amplitude);
}

function epiCycles(x, y, rotation, fourier) {
  for (let i = 1; i < fourier.length; i++) {
    let prevx = x;
    let prevy = y;
    let freq = fourier[i].freq;
    let radius = fourier[i].amplitude;
    let phase = fourier[i].phase;
    x += radius * cos(freq * time + phase + rotation);
    y += radius * sin(freq * time + phase + rotation);

    stroke(255, 100);
    noFill();
    ellipse(prevx, prevy, radius * 2);
    stroke(255);
    line(prevx, prevy, x, y);
  }
  return createVector(x, y);
}

function draw() {
  background(0);

  let vx = epiCycles(width / 2 + 300, 100, 0, fourierX);
  let vy = epiCycles(200, height / 2 + 100, HALF_PI, fourierY);
  let v = createVector(vx.x, vy.y);
  path.unshift(v);
  line(vx.x, vx.y, v.x, v.y);
  line(vy.x, vy.y, v.x, v.y);

  beginShape();
  noFill();
  for (let i = 0; i < path.length; i++) {
    vertex(path[i].x, path[i].y);
  }
  endShape();

  const dt = TWO_PI / fourierY.length;
  time += dt;

  if (path.length > x.length-60) {
    path.pop();
  }
}