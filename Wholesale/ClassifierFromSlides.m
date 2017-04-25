figure(1)
plot(x1(1:20),x2(1:20),'o')
hold on
plot(x1(26:45),x2(26:45),'x')
plot(x1(21:25),x2(21:25),'b*')
plot(x1(46:50),x2(46:50),'rd')
% Build training set
xt=[x1(1:20),x2(1:20);x1(26:45),x2(26:45)]';
xt = [ones(1,40);xt];
yt=[ones(1,20),-1*ones(1,20)];
lambda=0.001;
% Solve for w
w = inv(xt*xt'+lambda)*(xt*yt')
