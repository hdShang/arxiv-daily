---
layout: default
title: AMD-HookNet++: Evolution of AMD-HookNet with Hybrid CNN-Transformer Feature Enhancement for Glacier Calving Front Segmentation
---

# AMD-HookNet++: Evolution of AMD-HookNet with Hybrid CNN-Transformer Feature Enhancement for Glacier Calving Front Segmentation

**arXiv**: [2512.14639v1](https://arxiv.org/abs/2512.14639) | [PDF](https://arxiv.org/pdf/2512.14639.pdf)

**作者**: Fei Wu, Marcel Dreier, Nora Gourmelon, Sebastian Wind, Jianlin Zhang, Thorsten Seehaus, Matthias Braun, Andreas Maier, Vincent Christlein

**分类**: cs.CV

**发布日期**: 2025-12-16

**期刊**: IEEE Transactions on Geoscience and Remote Sensing (2025)

**DOI**: [10.1109/TGRS.2025.3642764](https://doi.org/10.1109/TGRS.2025.3642764)

---

## 💡 一句话要点

**提出AMD-HookNet++混合CNN-Transformer特征增强方法，用于合成孔径雷达图像中的冰川崩解前缘分割。**

🎯 **匹配领域**: **视觉里程计**

**关键词**: `冰川分割` `合成孔径雷达图像` `混合CNN-Transformer` `特征增强` `注意力机制` `像素级对比学习` `崩解前缘检测` `遥感图像分析`

## 📋 核心要点

1. 核心问题：纯CNN方法在冰川分割中难以捕获长距离依赖关系，导致全局上下文信息不足，影响崩解前缘的准确描绘。
2. 方法要点：提出混合CNN-Transformer架构，结合Transformer分支捕获全局上下文和CNN分支保留局部细节，并引入增强注意力模块优化特征交互。
3. 实验或效果：在CaFFe数据集上实现78.2 IoU和1,318米HD95，优于现有方法，并生成更平滑的前缘分割结果。

## 📝 摘要（中文）

冰川和冰架前缘的动态变化显著影响冰盖质量平衡和沿海海平面。为有效监测冰川状况，持续估计冰川崩解前缘的位置变化至关重要。AMD-HookNet首次引入了纯双分支卷积神经网络（CNN）进行冰川分割。然而，卷积操作的局部性和平移不变性虽然有利于捕捉低级细节，但限制了模型保持长距离依赖关系的能力。本研究提出AMD-HookNet++，一种新颖的先进混合CNN-Transformer特征增强方法，用于分割合成孔径雷达图像中的冰川并描绘崩解前缘。我们的混合结构包括两个分支：一个基于Transformer的上下文分支以捕获长距离依赖关系，在更大视图中提供全局上下文信息；一个基于CNN的目标分支以保留局部细节。为增强连接混合特征的表示，我们设计了一个增强的空间通道注意力模块，通过从空间和通道角度动态调整令牌关系，促进混合CNN-Transformer分支之间的交互。此外，我们开发了像素到像素对比深度监督，通过将像素级度量学习集成到冰川分割中，优化我们的混合模型。通过在具有挑战性的冰川分割基准数据集CaFFe上进行广泛实验和全面的定量与定性分析，我们表明AMD-HookNet++以78.2的IoU和1,318米的HD95设定了新的最先进水平，同时保持了367米的竞争性MDE。更重要的是，我们的混合模型产生了更平滑的崩解前缘描绘，解决了纯基于Transformer方法中常见的锯齿边缘问题。

## 🔬 方法详解

AMD-HookNet++采用双分支混合架构：一个基于Transformer的上下文分支用于捕获全局长距离依赖关系，提供大视图下的上下文信息；一个基于CNN的目标分支用于保留局部细节特征。关键技术创新包括增强的空间通道注意力模块，该模块通过动态调整空间和通道维度的令牌关系，促进两个分支之间的特征交互，从而优化混合特征的表示。此外，引入了像素到像素对比深度监督，将像素级度量学习集成到训练过程中，进一步提升分割精度。与现有方法的主要区别在于：相比纯CNN的AMD-HookNet，本方法通过Transformer分支弥补了长距离依赖的不足；相比纯Transformer方法，本方法通过CNN分支避免了锯齿边缘问题，实现了更平滑的分割结果。

## 📊 实验亮点

在CaFFe基准数据集上，AMD-HookNet++实现了78.2的IoU和1,318米的HD95，显著优于先前方法，同时保持367米的MDE；定性分析显示，模型能生成更平滑的崩解前缘分割，有效解决了纯Transformer方法的锯齿边缘问题。

## 🎯 应用场景

该研究主要应用于冰川监测和气候变化研究领域，通过高精度分割合成孔径雷达图像中的冰川崩解前缘，支持冰川动态变化分析、冰盖质量平衡评估和沿海海平面预测，具有重要的环境科学和地球观测价值。

## 📄 摘要（原文）

> The dynamics of glaciers and ice shelf fronts significantly impact the mass balance of ice sheets and coastal sea levels. To effectively monitor glacier conditions, it is crucial to consistently estimate positional shifts of glacier calving fronts. AMD-HookNet firstly introduces a pure two-branch convolutional neural network (CNN) for glacier segmentation. Yet, the local nature and translational invariance of convolution operations, while beneficial for capturing low-level details, restricts the model ability to maintain long-range dependencies. In this study, we propose AMD-HookNet++, a novel advanced hybrid CNN-Transformer feature enhancement method for segmenting glaciers and delineating calving fronts in synthetic aperture radar images. Our hybrid structure consists of two branches: a Transformer-based context branch to capture long-range dependencies, which provides global contextual information in a larger view, and a CNN-based target branch to preserve local details. To strengthen the representation of the connected hybrid features, we devise an enhanced spatial-channel attention module to foster interactions between the hybrid CNN-Transformer branches through dynamically adjusting the token relationships from both spatial and channel perspectives. Additionally, we develop a pixel-to-pixel contrastive deep supervision to optimize our hybrid model by integrating pixelwise metric learning into glacier segmentation. Through extensive experiments and comprehensive quantitative and qualitative analyses on the challenging glacier segmentation benchmark dataset CaFFe, we show that AMD-HookNet++ sets a new state of the art with an IoU of 78.2 and a HD95 of 1,318 m, while maintaining a competitive MDE of 367 m. More importantly, our hybrid model produces smoother delineations of calving fronts, resolving the issue of jagged edges typically seen in pure Transformer-based approaches.

