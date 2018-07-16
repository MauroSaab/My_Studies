function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values

%%% X = [ones(m, 1), data(:,1)]; 
% theta = zeros(2, 1); % initialize fitting parameters
% iterations = 1500;
% alpha = 0.01;
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %
	% X * theta   97x2 x 2x1 = 97x1
	e = (X * theta) - y     % 97x1 - 97x1 = 97x1
	temp0 = theta(1) - (alpha/m * sum(e))    
	temp1 = theta(2) - (alpha/m * sum(e.*X(:,2)))
	theta(1) = temp0
	theta(2) = temp1 

    % Save the cost J in every iteration    
	
    J_history(iter) = computeCost(X, y, theta);
	disp ("The present value of J is:"), disp (J_history(iter));
	
	% ============================================================
end

disp (J_history);

end
