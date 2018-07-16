function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%	neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. 
%
%	The parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% 	Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% 	for our 2 layer neural network

Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));
				 
% Setup some useful variables

m = size(X, 1);

% You need to return the following variables correctly 

J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%

% Vamos transformar o output Y para o formato requerido.
% Por exemplo, devemos transformar y = 2 em Y = [0 1 0 0 0 0 0 0 0 0]

I = eye(num_labels);
Y = zeros(m, num_labels);

for i = 1:m
	Y(i, :) = I(y(i), :);   % size 5000 x 10, organizado em linhas.
end

a1 = [ones(m, 1) X];    	 % a1 = X  (Só acrescentamos a coluna de 1s)
z2 = a1 * Theta1'; 			 % z2 = a1 * theta1
a2 = [ones(size(z2,1), 1) sigmoid(z2)]; % Acrescentamos uma coluna para a próxima linha fazer 
			%  ... sentido uma vez que Theta 2 possui uma dimensão a mais por conta do bias
z3 = a2 * Theta2';			 % z3 = a2 
a3 = sigmoid(z3);			 % a3 = hipótese
h = a3;

% Vamos agora implementar a função custo
% Para evitar uma expressão colossal, vamos calcular a Regularização separado:

% Vamos retirar a primeira coluna de cada matriz Theta uma vez que :

		% Note that you should not be regularizing the terms that correspond to
		% the bias. For the matrices Theta1 and Theta2, this corresponds to the 
		% first column of each matrix.

p = sum(sum(Theta1(:, 2:end).^2))+sum(sum(Theta2(:, 2:end).^2));

Reg = (lambda*p)/(2*m);

J = -1/m * sum(sum(Y.*log(h) + (1-Y).*log(1-h)));

J = J + Reg;


% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%

X = [ones(m, 1) X]; % Acrescentamos o BIAS

for k = 1:m
	
	a1 = X(k,:);		% Pegamos uma linha por vez (uma imagem das 5000) [1x401]
	z2 = Theta1 * a1';	% Calculamos z2 [25x401 * 401x1 = 25x1]
	
	a2 = sigmoid(z2);	% e através de z2, as ativações do Layer 2 [25x1]
	a2 = [1 ; a2];		% Acrescentamos seu BIAS [26x1]
	
	z3 = Theta2 * a2;	% Calculamos z3 [10x26 * 26x1] = [10x1]
	a3 = sigmoid(z3);   % e através de z3, as ativações do output Layer [10x1]
	
	d3 = a3 - Y(k, :)';  % através das quais calculamos o erro em relação ao esperado [10x1]
	
	z2 = [1; z2];		% Reintroduz-se o Bias para fins de Dimensão [26x1]
	d2 = (Theta2' * d3) .* sigmoidGradient(z2);  % 26x10 * 10x1 = 26x1 .* 26x1
	
	d2 = d2(2:end);  % Retira-se o Bias novamente após a operação acima.
	
	Theta2_grad = (Theta2_grad + (d3 * a2'));  % (10x1 * 1x26 = 10x26)
	Theta1_grad = (Theta1_grad + (d2 * a1));   % (25x1 * 1x401 = 25x401)

end

% WITH NO REGULARIZATION:

% Theta2_grad = Theta2_grad ./ m;
% Theta1_grad = Theta1_grad ./ m;

% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.

% Fórmula para Regularização:
	% D (ij) = 1/m * (Delta (ij) + lambda (ij) * Theta (ij)) 
		% para j > = 1

% Derivada de J em relação a cada Theta para a primeira Coluna (BIAS)

Theta1_grad(:,1) = Theta1_grad(:,1)./m;
Theta2_grad(:,1) = Theta2_grad(:,1)./m;

% Derivada de J em relação a cada Theta para as demais colunas (c/ regularização)

Theta1_grad(:,2:end) = Theta1_grad(:,2:end)./m + ( (lambda/m) * Theta1(:,2:end) );
Theta2_grad(:,2:end) = Theta2_grad(:,2:end)./m + ( (lambda/m) * Theta2(:,2:end) );

% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
