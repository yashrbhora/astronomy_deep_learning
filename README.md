# Deep Learning in the Context of Astronomy
Given my interests in the intersections of physics and machine learning, here's an ensemble of projects where I study and apply various deep learning techniques in the context of astronomy for my own practice and understanding.

## Current Projects
**Galaxy Classification**: Using CNNs to classify various galaxies into ten different types from the Galaxy10 DECals Dataset. With Josh Pierce, we initially explored Logistic Regression with PCA and a simple CNN to set a baseline accuracy. Then, on my own, I explored transfer learning with SOTA models and achieved much better performance. To set a stronger baseline that doesn't use deep learning, I used LightGBM which gave performance comparable to simple CNNS. Finally, I trained a more advanced CNN from scratch, armed with techniques like residual connections, batch normalization, and depthwise separable convolutions, to build a mini-xception model that performed similarly to SOTA models that used transfer learning. To see what's happening under the hood, I visualize intermediate activations and convnet filters of the mini-xception model.

**Neural Style Transfer**: This is more related to Deep Learning than  Astronomy/Astrophysics where I transfer the art styles of some of my favorite painters to images of celestial objects via neural style transfer.

**Variable Stars Classification (In Progress)**: I aim to classify variable stars using light-curve data and RNN autoencoders as described in [this paper.](https://www.nature.com/articles/s41550-017-0321-z)

*These are projects in which I aim to apply skills I learned from François Chollet's 'Deep Learning with Python (2nd Ed.)' to my personal interest in astronomy.*
