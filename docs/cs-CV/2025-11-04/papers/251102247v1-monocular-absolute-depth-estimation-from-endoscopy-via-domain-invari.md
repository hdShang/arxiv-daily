---
layout: default
title: Monocular absolute depth estimation from endoscopy via domain-invariant feature learning and latent consistency
---

# Monocular absolute depth estimation from endoscopy via domain-invariant feature learning and latent consistency

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.02247" class="toolbar-btn" target="_blank">📄 arXiv: 2511.02247v1</a>
  <a href="https://arxiv.org/pdf/2511.02247.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.02247v1" onclick="toggleFavorite(this, '2511.02247v1', 'Monocular absolute depth estimation from endoscopy via domain-invariant feature learning and latent consistency')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Li, Daiwei Lu, Jesse d'Almeida, Dilara Isik, Ehsan Khodapanah Aghdam, Nick DiSanto, Ayberk Acar, Susheela Sharma, Jie Ying Wu, Robert J. Webster, Ipek Oguz

**分类**: cs.CV

**发布日期**: 2025-11-04

**🔗 代码/项目**: [GITHUB](https://github.com/MedICL-VU/MDE)

---

## 💡 一句话要点

**提出基于特征对齐和潜在一致性的单目内窥镜绝对深度估计方法**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `单目深度估计` `内窥镜` `域自适应` `特征对齐` `对抗学习`

## 📋 核心要点

1. 现有方法难以从内窥镜图像中准确估计绝对深度，限制了医疗机器人的应用。
2. 该方法通过对抗学习和特征一致性，学习域不变的潜在特征，缩小合成图像和真实图像之间的域差距。
3. 实验表明，该方法在绝对和相对深度指标上均优于现有方法，并在不同骨干网络上表现出一致的提升。

## 📝 摘要（中文）

单目深度估计(MDE)是引导自主医疗机器人的关键任务。然而，从手术场景中的内窥镜相机获取绝对（度量）深度很困难，这限制了在真实内窥镜图像上进行深度监督学习。现有的图像级无监督域自适应方法将具有已知深度图的合成图像转换为真实内窥镜帧的风格，并使用这些转换后的图像及其对应的深度图来训练深度网络。然而，真实图像和转换后的合成图像之间通常仍然存在域差距。本文提出了一种潜在特征对齐方法，通过减少中央气道内窥镜视频中的这种域差距来提高绝对深度估计的性能。我们的方法与图像转换过程无关，专注于深度估计本身。具体来说，深度网络将转换后的合成图像和真实内窥镜帧作为输入，并通过对抗学习和定向特征一致性来学习潜在的域不变特征。在手动对齐绝对深度图的中央气道模型内窥镜视频上进行了评估。与最先进的MDE方法相比，我们的方法在绝对和相对深度指标上都取得了优异的性能，并且在各种骨干网络和预训练权重上都能持续提高结果。代码已开源。

## 🔬 方法详解

**问题定义**：论文旨在解决内窥镜视频中单目绝对深度估计的问题。现有方法，如图像级无监督域自适应，虽然尝试将合成图像转换为真实图像的风格，但仍然存在域差距，导致深度估计精度不高。直接在真实内窥镜图像上进行监督学习又缺乏精确的深度标注。

**核心思路**：核心思路是通过学习域不变的潜在特征来缩小合成图像和真实图像之间的域差距。通过对抗学习，使深度估计网络提取的特征在合成域和真实域之间难以区分，从而实现特征层面的对齐。同时，利用定向特征一致性约束，保证特征空间的一致性。

**技术框架**：整体框架包括图像转换模块（可选，用于生成风格更接近真实图像的合成图像）和深度估计网络。深度估计网络以转换后的合成图像和真实内窥镜图像作为输入，通过特征提取器提取特征，然后通过对抗学习模块和定向特征一致性模块进行训练。最终，深度估计网络输出深度图。

**关键创新**：关键创新在于提出了一种在潜在特征空间进行域对齐的方法，而不是直接在图像空间进行对齐。这种方法更加关注深度估计任务本身，能够更有效地提取域不变的特征。此外，定向特征一致性约束进一步增强了特征空间的一致性。

**关键设计**：对抗学习模块使用梯度反转层(GRL)来训练特征提取器，使其提取的特征难以被域判别器区分。定向特征一致性模块通过计算合成图像和真实图像特征之间的余弦相似度，并施加约束，使得相似度尽可能高。损失函数包括深度估计损失、对抗损失和特征一致性损失。具体的网络结构和参数设置根据不同的骨干网络进行调整。

## 📊 实验亮点

该方法在中央气道模型内窥镜视频上进行了评估，与最先进的单目深度估计方法相比，在绝对深度指标和相对深度指标上均取得了显著提升。实验结果表明，该方法在不同的骨干网络和预训练权重下都能稳定提升性能，证明了其鲁棒性和泛化能力。具体性能提升数据在论文中给出。

## 🎯 应用场景

该研究成果可应用于医疗机器人辅助手术，例如内窥镜手术导航、机器人臂的精确控制等。通过准确估计手术场景的深度信息，可以提高手术的安全性、精确性和效率。未来，该技术有望推广到其他医学影像领域，如CT、MRI等，为临床诊断和治疗提供更强大的支持。

## 📄 摘要（原文）

> Monocular depth estimation (MDE) is a critical task to guide autonomous medical robots. However, obtaining absolute (metric) depth from an endoscopy camera in surgical scenes is difficult, which limits supervised learning of depth on real endoscopic images. Current image-level unsupervised domain adaptation methods translate synthetic images with known depth maps into the style of real endoscopic frames and train depth networks using these translated images with their corresponding depth maps. However a domain gap often remains between real and translated synthetic images. In this paper, we present a latent feature alignment method to improve absolute depth estimation by reducing this domain gap in the context of endoscopic videos of the central airway. Our methods are agnostic to the image translation process and focus on the depth estimation itself. Specifically, the depth network takes translated synthetic and real endoscopic frames as input and learns latent domain-invariant features via adversarial learning and directional feature consistency. The evaluation is conducted on endoscopic videos of central airway phantoms with manually aligned absolute depth maps. Compared to state-of-the-art MDE methods, our approach achieves superior performance on both absolute and relative depth metrics, and consistently improves results across various backbones and pretrained weights. Our code is available at https://github.com/MedICL-VU/MDE.

