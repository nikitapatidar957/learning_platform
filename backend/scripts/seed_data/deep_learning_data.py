"""
Deep Learning seed data: Topics and Lessons.
Covers Perceptrons, Backprop, ANN Regression/Classification, OpenCV, CNNs, and Transfer Learning.
"""

DEEP_LEARNING_TOPICS = [
    {
        "subjectSlug": "deep-learning",
        "title": "Neural Network Fundamentals & Backprop",
        "slug": "neural-network-training",
        "description": "Perceptrons, multi-layer networks, activation functions, forward propagation, calculus chain rule backpropagation, and optimizers.",
        "order": 1,
        "isPublished": True,
    },
    {
        "subjectSlug": "deep-learning",
        "title": "ANN Regression & Classification with TensorFlow",
        "slug": "ann-tensorflow-modeling",
        "description": "Building and training multi-layer neural networks with Keras Sequential API, regression, classification, loss curves, and callbacks.",
        "order": 2,
        "isPublished": True,
    },
    {
        "subjectSlug": "deep-learning",
        "title": "Computer Vision with OpenCV",
        "slug": "opencv-computer-vision",
        "description": "Image and video processing with OpenCV: color spaces, filtering, blurring, Canny edge detection, thresholding, and contours.",
        "order": 3,
        "isPublished": True,
    },
    {
        "subjectSlug": "deep-learning",
        "title": "Convolutional Neural Networks & Augmentation",
        "slug": "cnn-computer-vision",
        "description": "Convolution filters, padding, stride, pooling layers, image folder generators, and data augmentation to prevent overfitting.",
        "order": 4,
        "isPublished": True,
    },
    {
        "subjectSlug": "deep-learning",
        "title": "Transfer Learning with Pretrained ConvNets",
        "slug": "transfer-learning-convnets",
        "description": "Leveraging ImageNet pretrained backbones (VGG, ResNet, MobileNet), feature extraction, fine-tuning, and global average pooling.",
        "order": 5,
        "isPublished": True,
    },
]

DEEP_LEARNING_LESSONS = [
    {
        "topicSlug": "neural-network-training",
        "subjectSlug": "deep-learning",
        "title": "Perceptrons & Multi-Layer Neural Networks",
        "slug": "perceptrons-multi-layer-networks",
        "description": "Understand the artificial neuron, linear combinations (z = Wx + b), and why non-linear activation functions are mandatory.",
        "estimatedTime": "25 mins",
        "difficulty": "Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "The Perceptron: Building Block of Deep Learning",
                    "content": (
                        "Proposed by Frank Rosenblatt in 1958, a perceptron models an individual biological neuron:\n\n"
                        "1. Inputs (x₁, x₂, ..., xₙ) are multiplied by respective Weights (w₁, w₂, ..., wₙ).\n"
                        "2. Weighted inputs are summed with a Bias term (b): z = Σ (wᵢ * xᵢ) + b.\n"
                        "3. The net input z is passed through an Activation Function a = σ(z) to produce the final output."
                    )
                },
                {
                    "type": "explanation",
                    "title": "Why Are Non-Linear Activation Functions Mandatory?",
                    "content": (
                        "Without non-linear activations (like ReLU, Sigmoid, Tanh), a 100-layer neural network is mathematically identical to a single 1-layer linear regression! "
                        "Because the combination of linear functions is always just another linear function: W₂(W₁x) = (W₂W₁)x = W_combined x.\n\n"
                        "Non-linearities allow the network to approximate any continuous function (Universal Approximation Theorem), "
                        "bending decision boundaries around complex non-linear patterns."
                    )
                },
                {
                    "type": "code",
                    "title": "Popular Activation Functions in Python",
                    "language": "python",
                    "code": (
                        "import numpy as np\n\n"
                        "# 1. ReLU (Rectified Linear Unit): Standard in hidden layers (prevents vanishing gradients)\n"
                        "def relu(z):\n"
                        "    return np.maximum(0, z)\n\n"
                        "# 2. Sigmoid: Outputs probability in [0, 1] (binary classification output layer)\n"
                        "def sigmoid(z):\n"
                        "    return 1 / (1 + np.exp(-z))\n\n"
                        "# 3. Softmax: Outputs probability distribution over k classes (sum = 1.0)\n"
                        "def softmax(z):\n"
                        "    exp_z = np.exp(z - np.max(z))\n"
                        "    return exp_z / np.sum(exp_z)"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "neural-network-training",
        "subjectSlug": "deep-learning",
        "title": "Forward Propagation, Loss & Backpropagation",
        "slug": "forward-backpropagation-chain-rule",
        "description": "Master forward activation computation, cross-entropy loss, and computing weight gradients via the calculus chain rule.",
        "estimatedTime": "35 mins",
        "difficulty": "Intermediate to Advanced",
        "order": 2,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Forward Pass vs Backward Pass",
                    "content": (
                        "• Forward Propagation: Input features flow layer by layer through linear transforms and activation functions to compute predicted probabilities ŷ, "
                        "and compare with actual target y using a Loss Function (e.g., Binary Cross-Entropy).\n\n"
                        "• Backward Propagation: The process of propagating the error backwards from the output layer to early layers using the Calculus Chain Rule, "
                        "calculating the partial derivative of Loss with respect to every single weight: ∂L/∂W."
                    )
                },
                {
                    "type": "explanation",
                    "title": "The Chain Rule in Action",
                    "content": (
                        "For a 2-layer network: Input x ➔ Layer 1 (z₁ = W₁x, a₁ = σ(z₁)) ➔ Layer 2 (z₂ = W₂a₁, ŷ = σ(z₂)) ➔ Loss L(y, ŷ).\n\n"
                        "To compute how changing weight W₁ affects the final Loss L, we chain the gradients:\n\n"
                        "∂L / ∂W₁ = (∂L / ∂ŷ) * (∂ŷ / ∂z₂) * (∂z₂ / ∂a₁) * (∂a₁ / ∂z₁) * (∂z₁ / ∂W₁)\n\n"
                        "Each layer computes its local gradient and passes the incoming error gradient back to the preceding layer."
                    )
                },
                {
                    "type": "callout",
                    "variant": "info",
                    "content": "Modern Optimizers: SGD (basic), Momentum (accelerates in consistent directions), RMSProp (adapts learning rate per parameter), Adam (Adaptive Moment Estimation: combines Momentum + RMSProp, the industry standard)."
                }
            ]
        }
    },
    {
        "topicSlug": "ann-tensorflow-modeling",
        "subjectSlug": "deep-learning",
        "title": "Artificial Neural Networks: Regression & Classification with TensorFlow",
        "slug": "tensorflow-ann-regression-and-classification",
        "description": "Master multi-layer perceptron (MLP) architecture design, loss formulation, model compilation, training loops, and evaluation in TensorFlow.",
        "estimatedTime": "45 mins",
        "difficulty": "Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Keras Sequential API & Model Lifecycle",
                    "content": (
                        "TensorFlow's high-level Keras API simplifies deep learning into 4 reproducible steps:\n\n"
                        "1. **Define Architecture**: Stack layers using `tf.keras.Sequential`.\n"
                        "2. **Compile Model**: Specify the loss function (`loss='mae'` or `loss='categorical_crossentropy'`), optimizer (`optimizer=tf.keras.optimizers.Adam(learning_rate=0.001)`), and evaluation metrics.\n"
                        "3. **Fit / Train**: Run gradient descent over epochs with validation splits and callbacks.\n"
                        "4. **Evaluate & Predict**: Measure out-of-sample performance and generate predictions."
                    )
                },
                {
                    "type": "code",
                    "title": "Building a Classification Neural Network with Callbacks",
                    "language": "python",
                    "code": (
                        "import tensorflow as tf\n\n"
                        "model = tf.keras.Sequential([\n"
                        "    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),\n"
                        "    tf.keras.layers.Dropout(0.2),\n"
                        "    tf.keras.layers.Dense(32, activation='relu'),\n"
                        "    tf.keras.layers.Dense(1, activation='sigmoid')\n"
                        "])\n\n"
                        "model.compile(\n"
                        "    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),\n"
                        "    loss='binary_crossentropy',\n"
                        "    metrics=['accuracy', tf.keras.metrics.AUC(name='auc')]\n"
                        ")\n\n"
                        "early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)\n"
                        "history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, callbacks=[early_stop])"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "opencv-computer-vision",
        "subjectSlug": "deep-learning",
        "title": "Computer Vision Fundamentals with OpenCV",
        "slug": "opencv-computer-vision-fundamentals",
        "description": "Master image and video processing with OpenCV: color spaces (BGR to RGB/HSV), filtering, Canny edge detection, thresholding, and contours.",
        "estimatedTime": "40 mins",
        "difficulty": "Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "OpenCV Foundations: Image Representation & Color Spaces",
                    "content": (
                        "OpenCV treats images as NumPy multi-dimensional arrays where:\n\n"
                        "• Grayscale: 2D array of pixel intensities from 0 (black) to 255 (white).\n"
                        "• Color (BGR): 3D array of shape `(Height, Width, 3)` with Blue, Green, Red channels.\n\n"
                        "Crucial Rule: OpenCV reads images in **BGR** format. Always convert to **RGB** with `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)` before displaying in matplotlib!"
                    )
                },
                {
                    "type": "code",
                    "title": "Canny Edge Detection and Contour Finding",
                    "language": "python",
                    "code": (
                        "import cv2\n\n"
                        "# Load and convert to grayscale\n"
                        "img = cv2.imread('sample.jpg')\n"
                        "gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)\n\n"
                        "# Apply Gaussian Blur to eliminate high-frequency noise\n"
                        "blurred = cv2.GaussianBlur(gray, (5, 5), 0)\n\n"
                        "# Multi-stage Canny Edge Detector\n"
                        "edges = cv2.Canny(blurred, threshold1=50, threshold2=150)\n\n"
                        "# Extract contours\n"
                        "contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)\n"
                        "print(f'Total objects detected: {len(contours)}')"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "cnn-computer-vision",
        "subjectSlug": "deep-learning",
        "title": "Convolutional Neural Networks (CNN) & Image Augmentation",
        "slug": "convolutional-neural-networks-and-computer-vision",
        "description": "Deep dive into Convolutional Neural Networks: convolution operations, kernels, stride, padding, pooling, and data augmentation to prevent overfitting.",
        "estimatedTime": "45 mins",
        "difficulty": "Intermediate to Advanced",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Convolutional Layer Mechanics & Spatial Filtering",
                    "content": (
                        "Convolutional layers apply small learnable filters/kernels (e.g. 3x3) sliding across the input image:\n\n"
                        "• **Parameter Sharing**: The same filter is applied across the entire image, drastically reducing weight counts compared to dense layers.\n"
                        "• **Translation Invariance**: Detects edges, textures, and patterns regardless of their spatial location.\n"
                        "• **Output Dimension Formula**: `Output = ((Input - Kernel + 2*Padding) / Stride) + 1`.\n"
                        "• **MaxPooling2D**: Downsamples spatial dimensions (e.g. 2x2 with stride 2 cuts height and width in half), preserving dominant activations."
                    )
                },
                {
                    "type": "code",
                    "title": "Modern CNN with Image Augmentation",
                    "language": "python",
                    "code": (
                        "import tensorflow as tf\n"
                        "from tensorflow.keras import layers, models\n\n"
                        "# Data Augmentation Pipeline\n"
                        "data_augmentation = tf.keras.Sequential([\n"
                        "    layers.RandomFlip('horizontal'),\n"
                        "    layers.RandomRotation(0.2),\n"
                        "    layers.RandomZoom(0.2),\n"
                        "])\n\n"
                        "# Convolutional Architecture\n"
                        "model = models.Sequential([\n"
                        "    layers.Input(shape=(128, 128, 3)),\n"
                        "    data_augmentation,\n"
                        "    layers.Rescaling(1./255),\n"
                        "    layers.Conv2D(32, (3, 3), activation='relu'),\n"
                        "    layers.MaxPooling2D((2, 2)),\n"
                        "    layers.Conv2D(64, (3, 3), activation='relu'),\n"
                        "    layers.MaxPooling2D((2, 2)),\n"
                        "    layers.Conv2D(128, (3, 3), activation='relu'),\n"
                        "    layers.GlobalAveragePooling2D(),\n"
                        "    layers.Dense(64, activation='relu'),\n"
                        "    layers.Dense(10, activation='softmax')\n"
                        "])"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "transfer-learning-convnets",
        "subjectSlug": "deep-learning",
        "title": "Transfer Learning with Pretrained ConvNets",
        "slug": "transfer-learning-with-pretrained-convnets",
        "description": "Master transfer learning workflows: utilizing ImageNet pretrained backbones (MobileNet, ResNet, VGG), feature extraction, and fine-tuning.",
        "estimatedTime": "45 mins",
        "difficulty": "Advanced",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Feature Extraction vs Fine-Tuning",
                    "content": (
                        "Transfer learning reuses knowledge from models pretrained on ImageNet (1.4 million images across 1000 categories):\n\n"
                        "• **Feature Extraction**:\n"
                        "  1. Instantiate base model without top layer: `base_model = MobileNetV2(include_top=False, weights='imagenet')`.\n"
                        "  2. Freeze base layers: `base_model.trainable = False`.\n"
                        "  3. Add custom classification head (`GlobalAveragePooling2D() -> Dense(num_classes)`).\n"
                        "  4. Train only head parameters.\n\n"
                        "• **Fine-Tuning**:\n"
                        "  1. After head converges, unfreeze top convolutional blocks of the base model.\n"
                        "  2. Recompile with an ultra-low learning rate (e.g. `1e-5`) to fine-tune high-level representations without destroying pretrained weights."
                    )
                },
                {
                    "type": "code",
                    "title": "Transfer Learning with MobileNetV2 in Keras",
                    "language": "python",
                    "code": (
                        "import tensorflow as tf\n\n"
                        "base_model = tf.keras.applications.MobileNetV2(\n"
                        "    input_shape=(224, 224, 3),\n"
                        "    include_top=False,\n"
                        "    weights='imagenet'\n"
                        ")\n"
                        "base_model.trainable = False\n\n"
                        "inputs = tf.keras.Input(shape=(224, 224, 3))\n"
                        "x = tf.keras.applications.mobilenet_v2.preprocess_input(inputs)\n"
                        "x = base_model(x, training=False)\n"
                        "x = tf.keras.layers.GlobalAveragePooling2D()(x)\n"
                        "x = tf.keras.layers.Dropout(0.2)(x)\n"
                        "outputs = tf.keras.layers.Dense(5, activation='softmax')(x)\n"
                        "model = tf.keras.Model(inputs, outputs)\n\n"
                        "model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])"
                    )
                }
            ]
        }
    },
]
