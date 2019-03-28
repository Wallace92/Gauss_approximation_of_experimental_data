# Gauss_approximation_of_experimental_data
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">

</head>
<body>
 The program uses the scipy stats library to aproximate the data using normal distribution <br>
  
<ul>
  <li>"The equation of Gauss distribution </li>
  <p>
  $$   f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp{-\frac{(x-\mu)^2}{2\sigma^2}} $$ 
    
   where $ \mu $ is mean of all data, $ \sigma $ denote standard deviation
</p>
  <li>The standar deviation is expressed as:
  
  $$ \sigma = \frac{\sum_{i=1}^N (x_i - \mu)}{N} $$

</li>
  <li>The Gauss distribution very well fit many experimental data and determine the probability of occurence each of it</li>
</ul>
Finally the roots are presented using matplotlib with beatiful latex graphics. The straigh line at the middle shows the mean value of approximated data.
</body>
</html>
