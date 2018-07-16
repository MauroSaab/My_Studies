function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 

J = 0;
n = columns(X) - 1;
total = 0;
soma = 0;
soma2 = 0;
soma3 = 0;
soma4 = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta

%%%%%%%%%%%%%%%%%%%%%%% COST FUNCTION

for iter = 1:m  % PARA CADA LINHA DE ENTRADA
	h = sigmoid(X(iter,:)*theta) % CALCULAMOS A HIPÓTESE
	part = (-y(iter) * log(h)) - ((1-y(iter))*log(1-(h))) % CALCULAMOS OS ERROS
	soma = soma + part % SOMAMOS A PARCELA NO SOMATÓRIO
end

for iter = 2:length(theta)
	parc3 = theta(iter)**2
	soma3 = soma3 + parc3
end

J = (1/m) * soma + (lambda/(2*m)) * soma3

%%%%%%%%%%%%%%%%%%%%%%% GRADIENTE 

for iter2 = 1:n+1 % PARA CADA FEATURE
	soma2 = 0;   % RESETAMOS soma2
	for iter = 1:m % PARA CADA LINHA  (LAÇO Q PREENCHE SOMA2)
		h = sigmoid(X(iter,:)*theta)  % CALCULAMOS A HIPÓTESE
		part2 = (h-y(iter))*X(iter,iter2) % CALCULAMOS O ERRO
		soma2 = soma2 + part2 % E ACRESCENTAMOS A PARCELA NO SOMATÓRIO
	end
	
	if (iter2 == 1) 
		grad(iter2) = (1/m) * soma2
	else
		soma4 = 0;
		parc4 = (lambda/m) * theta(iter2)
		soma4 = soma4 + parc4
		grad(iter2) = (1/m) * soma2 + soma4
end


end
	