clear

opts = odeset("MaxStep", 1e-1);
[t, x] = ode45(@walking_orbit_dyn, [0 6*100], [0.0; 0.0; 0.0], opts);

data = [ t x ];
save result data

figure(1)
plot(t, x(:, 1))
xlabel("time(s)")
ylabel("x(m)")
grid on

figure(2)
plot(t, x(:, 2))
xlabel("time(s)")
ylabel("y(m)")
grid on

figure(3)
plot(t, x(:, 3)*180/pi)
xlabel("time(s)")
ylabel("theta(deg)")
grid on