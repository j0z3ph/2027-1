% promedio.m
% Pide al usuario 5 numeros y obtiene el promedio
% Autor: Jose Luis
% Fecha: 2026/11/27

clear;
clc;

numero = input('Usuario, ingresa 5 numeros: ');
prom = mean(numero);
%disp('El promedio es: ');
%disp(prom);
fprintf('El promedio es: %+20.2f.\n', prom);

