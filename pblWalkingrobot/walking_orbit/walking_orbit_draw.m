%load result
load result

% draw mode
draw_mode = 1;

% animation speed
ani_sample = 30;

% states
xc = x(:, 1);
yc = x(:, 2);
theta = x(:, 3);

% draw axes
figure(4)
clf
field_size = 4;
axis([-field_size field_size -field_size field_size])
axis square
grid on
line([-field_size field_size], [0 0], 'Color', 'k');
line([0 0], [-field_size field_size], 'Color', 'k');
xlabel('x (m)')
ylabel('y (m)')

% draw the initial pose
[xf, yf] = calFramePoints(xc(1), yc(1), theta(1));
frame_line = drawMobileRobot(xc(1), yc(1), xf, yf);

% animate the pose
for i = 2:ani_sample:length(t)
    [xf, yf] = calFramePoints(xc(i), yc(i), theta(i));
    if draw_mode == 0
        updateDrawMobileRobot(xc(i), yc(i), xf, yf, frame_line);
    else
        drawMobileRobot(xc(i), yc(i), xf, yf);
    end
    drawnow
end

% draw the final pose
[xf, yf] = calFramePoints(xc(length(t)), yc(length(t)), theta(length(t)));
if draw_mode == 0
    updateDrawMobileRobot(xc(i), yc(i), xf, yf, frame_line);
else
    drawMobileRobot(xc(i), yc(i), xf, yf);
end
drawnow


% definition of the functions
function [xf, yf] = calFramePoints(xc, yc, theta)
    % parameters of mobile robot
    len = 0.15;  % length [m]
    wid = 0.15;  % width [m]
    
    xf(1) = xc + len/2 * cos(theta);
    yf(1) = yc + len/2 * sin(theta);
    xf(2) = xf(1) + wid/2 * cos(theta + pi/2);
    yf(2) = yf(1) + wid/2 * sin(theta + pi/2);
    xf(3) = xf(2) + len * cos(theta + pi);
    yf(3) = yf(2) + len * sin(theta + pi);
    xf(4) = xf(3) + wid * cos(theta + 3*pi/2);
    yf(4) = yf(3) + wid * sin(theta + 3*pi/2);
    xf(5) = xf(4) + len * cos(theta);
    yf(5) = yf(4) + len * sin(theta);
end

function frame_line = drawMobileRobot(xc, yc, xf, yf)
    frame_line(1) = line([xc xf(1)], [yc yf(1)], 'Color', 'r', 'Linewid', 2);
    frame_line(2) = line([xf(2) xf(3)], [yf(2) yf(3)], 'Color', 'k', 'Linewid', 1);
    frame_line(3) = line([xf(3) xf(4)], [yf(3) yf(4)], 'Color', 'k', 'Linewid', 1);
    frame_line(4) = line([xf(4) xf(5)], [yf(4) yf(5)], 'Color', 'k', 'Linewid', 1);
    frame_line(5) = line([xf(5) xf(2)], [yf(5) yf(2)], 'Color', 'k', 'Linewid', 1);
end

function updateDrawMobileRobot(xc, yc, xf, yf, frame_line)
    set(frame_line(1), 'XData', [xc xf(1)], 'YData', [yc yf(1)]);
    set(frame_line(2), 'XData', [xf(2) xf(3)], 'YData', [yf(2) yf(3)]);
    set(frame_line(3), 'XData', [xf(3) xf(4)], 'YData', [yf(3) yf(4)]);
    set(frame_line(4), 'XData', [xf(4) xf(5)], 'YData', [yf(4) yf(5)]);
    set(frame_line(5), 'XData', [xf(5) xf(2)], 'YData', [yf(5) yf(2)]);
end