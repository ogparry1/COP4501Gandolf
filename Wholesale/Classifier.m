% Create a two-cluster data set with 100 points in each cluster
N = 100;
X1 = 0.3*bsxfun(@plus, randn(N, 2), [6 6]);
X2 = 0.6*bsxfun(@plus, randn(N, 2), [-2 -1]);

% Create a 200 by 3 data matrix similar to the one you have
% (see note below why 200 by 3 and not 200 by 2)
X = [[X1; X2] ones(2*N, 1)];

% Create 200 by 1 vector containing 1 for each point in the first cluster
% and -1 for each point in the second cluster
b = [ones(N, 1); -ones(N, 1)]

% Solve least squares problem
z = lsqlin(X, b);

% Plot data points and linear separator found above
y = -z(3)/z(2) - (z(1)/z(2))*x;
hold on;
plot(X(:, 1), X(:, 2), 'bx'); xlim([-3 3]); ylim([-3 3]);
plot(x, y, 'r');
