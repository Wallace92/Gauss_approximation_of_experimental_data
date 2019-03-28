# Gauss_approximation_of_experimental_data
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">

</head>
<body>
 The program contains three functions: <br>
  
<ul>
  <li>"equation" with the solved equation in this case </li>
  <p>
  $$   f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp{-\frac{(x-\mu)^2}{2\sigma^2}} $$
</p>
  <li>"bisection" the bisection algorithm that looking forward the roots at some interval with precision defied by number of iterations</li>
  <li>"interval" defines how dense the interval it is and perform the bisecion algorithm on each segment</li>
</ul>
Finally the roots are presented using matplotlib with beatiful latex graphics. The roots are marked with big doots and the values are printes in the console.
</body>
</html>
