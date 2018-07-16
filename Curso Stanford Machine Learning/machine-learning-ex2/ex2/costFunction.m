function [J, grad] = costFunction(theta, X, y)
%COSTFUNCTION Compute cost and gradient for logistic regression
%   J = COSTFUNCTION(theta, X, y) computes the cost of using theta as the
%   parameter for logistic regression and the gradient of the cost
%   w.r.t. to the parameters.

% Initialize some useful values
m = length(y); % number of training examples
n = columns(X) - 1;
total = 0;
soma = 0;
soma2 = 0;

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
%
% Note: grad should have the same dimensions as theta [theta = zeros(n + 1, 1)]

for iter = 1:m  % PARA CADA LINHA (TRAINING EXAMPLE) DO DATASET
	h = sigmoid(X(iter,:)*theta) % Calculamos X*Theta e aplicamos a função sigmóide obtendo a hipótese h
	part = (-y(iter) * log(h)) - ((1-y(iter))*log(1-(h))) % Calculamos a parcela do Somatório relativa à essa linha
	soma = soma + part	% E somamos a parcela no total
end

J = 1/m * soma % A Cost Function é 1/m * o Somatório

for iter2 = 1:n+1 % PARA CADA FEATURE DO DATASET
	soma2 = 0;	% Resetamos soma2
	for iter = 1:m   % PARA CADA LINHA DO DATASET
		h = sigmoid(X(iter,:)*theta) % Calculamos X*Theta e aplicamos a função sigmóide, obtendo a hipótese h
		part2 = (h-y(iter))*X(iter,iter2) % Calculamos a parcela do Somatório do Gradiente relativa à essa linha
		soma2 = soma2 + part2  % E somamos a parcela no total
	end	

	grad(iter2) = 1/m * soma2 % Aquele elemento da Matriz Gradiente será igual ao 1/m * o Somatório para aquela linha.
	
end

end
