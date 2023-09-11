[D,V] = eig(XLS)
[m,n] = size(XLS);
sum = zeros(m,n);

for i=1:m
    for j=1:n
        sum(1,i) = sum(1,i)+D(j,i);
    end
end

for i=1:m
    for j=1:n
        D1(i,j)=D(i,j)./sum(1,j);
    end
end
