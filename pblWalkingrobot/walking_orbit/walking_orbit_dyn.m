function dxdt = walking_orbit_dyn(t,x)

xc = x(1);
yc = x(2);
theta = x(3);

T = 4;
step = 7;
l = 0.09;
d = 0.15;

% you can change the parameter
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
if rem(ceil(t/40),2) == 0
    [dphiR, dphiL] = differencePhase(pi/12, pi/8);
else
    [dphiR, dphiL] = differencePhase(pi/8, pi/12);
end
%}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

dx1dt = step*l*bin(t)*(sqrt(2*(1-cos(dphiL))) + sqrt(2*(1-cos(dphiR))))*cos(theta)/(2*T);
dx2dt = step*l*bin(t)*(sqrt(2*(1-cos(dphiL))) + sqrt(2*(1-cos(dphiR))))*sin(theta)/(2*T);
dx3dt = step*l*bin(t)*(sqrt(2*(1-cos(dphiR))) - sqrt(2*(1-cos(dphiL))))/(d*T);

dxdt = [dx1dt; dx2dt; dx3dt];

    function s = outstep(i)
        i = fix(i);
        s = rem(i,T);
        if s <= T*1/step
            s = 1;
        elseif s <= T*2/step
            s = 2;
        elseif s <= T*3/step
            s = 3;
        elseif s <= T*4/step
            s = 4;
        elseif s <= T*5/step
            s = 5;
        elseif s <= T*6/step
            s = 6;
        else
            s = 7;
        end
    end

    function b = bin(i)
        b = outstep(i);
        if b == 4
            b = 1;
        else
            b = 0;
        end
    end

    function [dR, dL] = differencePhase(d1, d2)
        dR = d1;
        dL = d2;
    end

end