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

**提出AMD-HookNet++，通过混合CNN-Transformer特征增强解决冰川崩解前沿分割中长程依赖与局部细节平衡问题。**

🎯 **匹配领域**: **视觉里程计**

**关键词**: `冰川分割` `崩解前沿描绘` `混合CNN-Transformer` `特征增强` `空间-通道注意力` `像素对比学习` `合成孔径雷达` `遥感图像分析`

## 📋 核心要点

1. 核心问题：现有纯CNN方法在冰川分割中难以平衡局部细节与长程依赖，导致崩解前沿描绘不准确。
2. 方法要点：提出混合CNN-Transformer架构，结合Transformer捕获全局上下文和CNN保留局部细节，增强特征表示。
3. 实验或效果：在CaFFe数据集上，IoU达78.2，HD95为1,318米，崩解前沿描绘更平滑，优于现有方法。

## 📝 摘要（中文）

冰川和冰架前沿的动态变化对冰盖质量平衡和沿海海平面有显著影响。为有效监测冰川状况，持续估计冰川崩解前沿的位置变化至关重要。AMD-HookNet首次引入纯双分支卷积神经网络（CNN）进行冰川分割，但卷积操作的局部性和平移不变性虽有利于捕捉低层细节，却限制了模型保持长程依赖的能力。本研究提出AMD-HookNet++，一种新颖的先进混合CNN-Transformer特征增强方法，用于合成孔径雷达图像中的冰川分割和崩解前沿描绘。我们的混合结构包括两个分支：一个基于Transformer的上下文分支以捕获长程依赖，提供更大视野的全局上下文信息；一个基于CNN的目标分支以保留局部细节。为增强连接混合特征的表示，我们设计了一个增强的空间-通道注意力模块，通过从空间和通道角度动态调整令牌关系，促进混合CNN-Transformer分支之间的交互。此外，我们开发了像素到像素对比深度监督，通过将像素级度量学习集成到冰川分割中，优化我们的混合模型。通过在具有挑战性的冰川分割基准数据集CaFFe上进行广泛实验和全面的定量与定性分析，我们表明AMD-HookNet++以78.2的IoU和1,318米的HD95设定了新的最先进水平，同时保持了367米的竞争性MDE。更重要的是，我们的混合模型产生了更平滑的崩解前沿描绘，解决了纯基于Transformer方法中常见的锯齿边缘问题。

## 🔬 方法详解

**问题定义**：论文旨在解决冰川崩解前沿分割问题，特别是在合成孔径雷达图像中。现有方法如纯CNN（如AMD-HookNet）虽能捕捉局部细节，但由于卷积操作的局部性和平移不变性，难以建模长程依赖，导致崩解前沿描绘可能不连续或锯齿状，影响分割精度。

**核心思路**：论文提出混合CNN-Transformer架构，核心思想是结合CNN的局部细节捕捉能力和Transformer的全局上下文建模能力，以平衡特征表示。通过双分支设计，分别处理局部和全局信息，并引入注意力机制增强分支间交互，从而提升分割性能。

**技术框架**：整体架构包括两个主要分支：一个基于Transformer的上下文分支，用于捕获长程依赖和全局上下文信息；一个基于CNN的目标分支，用于保留局部细节和空间结构。两个分支的特征通过增强的空间-通道注意力模块进行融合，该模块动态调整空间和通道维度的令牌关系。此外，采用像素到像素对比深度监督，集成像素级度量学习以优化模型训练。

**关键创新**：最重要的技术创新是混合CNN-Transformer特征增强方法，特别是增强的空间-通道注意力模块。与现有纯CNN或纯Transformer方法相比，本质区别在于同时利用CNN的局部性和Transformer的全局性，通过注意力机制实现自适应特征融合，解决了长程依赖与局部细节的平衡问题。

**关键设计**：关键设计包括：双分支网络结构，其中Transformer分支可能基于Vision Transformer变体，CNN分支基于卷积层；增强的空间-通道注意力模块，通过多头注意力机制处理空间和通道维度；损失函数结合交叉熵损失和对比损失，用于像素级监督；参数设置如学习率、批量大小通过实验优化，具体数值未在摘要中提供，但模型在CaFFe数据集上训练和评估。

## 📊 实验亮点

在CaFFe基准数据集上，AMD-HookNet++取得了最先进的性能：IoU达到78.2，HD95为1,318米，同时MDE保持在367米的竞争水平。与基线方法相比，IoU和HD95均有显著提升，崩解前沿描绘更平滑，解决了纯Transformer方法的锯齿边缘问题。定量和定性分析均验证了混合模型的有效性。

## 🎯 应用场景

该研究主要应用于冰川监测和气候变化研究领域，通过高精度分割冰川崩解前沿，有助于实时跟踪冰川动态变化、评估冰盖质量平衡和预测海平面上升。实际价值在于提供自动化工具，减少人工标注成本，提升监测效率。未来可能扩展到其他遥感图像分割任务，如冰架、海冰监测，对环境保护和灾害预警有重要影响。

## 📄 摘要（原文）

> The dynamics of glaciers and ice shelf fronts significantly impact the mass balance of ice sheets and coastal sea levels. To effectively monitor glacier conditions, it is crucial to consistently estimate positional shifts of glacier calving fronts. AMD-HookNet firstly introduces a pure two-branch convolutional neural network (CNN) for glacier segmentation. Yet, the local nature and translational invariance of convolution operations, while beneficial for capturing low-level details, restricts the model ability to maintain long-range dependencies. In this study, we propose AMD-HookNet++, a novel advanced hybrid CNN-Transformer feature enhancement method for segmenting glaciers and delineating calving fronts in synthetic aperture radar images. Our hybrid structure consists of two branches: a Transformer-based context branch to capture long-range dependencies, which provides global contextual information in a larger view, and a CNN-based target branch to preserve local details. To strengthen the representation of the connected hybrid features, we devise an enhanced spatial-channel attention module to foster interactions between the hybrid CNN-Transformer branches through dynamically adjusting the token relationships from both spatial and channel perspectives. Additionally, we develop a pixel-to-pixel contrastive deep supervision to optimize our hybrid model by integrating pixelwise metric learning into glacier segmentation. Through extensive experiments and comprehensive quantitative and qualitative analyses on the challenging glacier segmentation benchmark dataset CaFFe, we show that AMD-HookNet++ sets a new state of the art with an IoU of 78.2 and a HD95 of 1,318 m, while maintaining a competitive MDE of 367 m. More importantly, our hybrid model produces smoother delineations of calving fronts, resolving the issue of jagged edges typically seen in pure Transformer-based approaches.

