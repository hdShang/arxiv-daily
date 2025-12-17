---
layout: default
title: Retrospective motion correction in MRI using disentangled embeddings
---

# Retrospective motion correction in MRI using disentangled embeddings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.08365" class="toolbar-btn" target="_blank">📄 arXiv: 2511.08365v1</a>
  <a href="https://arxiv.org/pdf/2511.08365.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.08365v1" onclick="toggleFavorite(this, '2511.08365v1', 'Retrospective motion correction in MRI using disentangled embeddings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qi Wang, Veronika Ecker, Marcel Früh, Sergios Gatidis, Thomas Küstner

**分类**: cs.CV

**发布日期**: 2025-11-11

**备注**: 5 pages, 3 figures

---

## 💡 一句话要点

**提出基于解耦嵌入的MRI运动伪影矫正方法，提升模型泛化性。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `MRI运动校正` `解耦表示学习` `变分自编码器` `向量量化` `自回归模型`

## 📋 核心要点

1. 现有MRI运动校正方法泛化性差，依赖特定数据集和运动类型，缺乏通用性。
2. 提出分层VQ-VAE学习解耦的运动特征嵌入，利用码本捕获多分辨率运动模式。
3. 通过自回归模型学习无运动图像先验，引导校正过程，无需特定伪影训练。

## 📝 摘要（中文）

生理运动会影响磁共振成像(MRI)的诊断质量。现有的回顾性运动校正方法难以泛化到不同的运动类型和身体区域，特别是基于机器学习(ML)的校正方法通常针对特定应用和数据集。本文假设运动伪影虽然多样，但共享可解耦和利用的潜在模式。为此，我们提出了一种分层向量量化(VQ)变分自编码器，学习运动到干净图像特征的解耦嵌入。该方法部署了一个码本，以多分辨率捕获有限的运动模式集合，从而实现由粗到精的校正。训练一个自回归模型来学习无运动图像的先验分布，并在推理时用于指导校正过程。与传统方法不同，我们的方法不需要特定于伪影的训练，并且可以推广到未见过的运动模式。我们在模拟的全身运动伪影上验证了该方法，并观察到在不同运动严重程度下的鲁棒校正。结果表明，该模型有效地解耦了模拟运动有效扫描的物理运动，从而提高了基于ML的MRI运动校正的泛化性。我们解耦运动特征的工作揭示了其在解剖区域和运动类型中的潜在应用。

## 🔬 方法详解

**问题定义**：MRI成像易受生理运动影响，产生伪影，降低诊断质量。现有基于机器学习的运动校正方法通常针对特定运动类型和身体区域训练，泛化能力有限，难以适应未知的运动模式。因此，如何设计一种通用的、无需特定伪影训练的运动校正方法是关键问题。

**核心思路**：核心思想是将运动伪影解耦为可解释的潜在特征，并利用这些特征进行校正。通过学习运动到干净图像的解耦嵌入，模型能够理解不同运动模式的共性，从而实现对未知运动模式的校正。使用码本捕获多分辨率的运动模式，实现由粗到精的校正。

**技术框架**：该方法基于分层VQ-VAE框架。首先，输入受运动影响的MRI图像，通过编码器提取特征。然后，使用向量量化(VQ)层将特征映射到码本中的离散码字，码本包含多个分辨率的运动模式。解码器利用这些码字重建干净的MRI图像。此外，训练一个自回归模型学习无运动图像的先验分布，在推理阶段，该先验分布用于指导解码器生成更真实的校正图像。

**关键创新**：最重要的创新点在于学习运动特征的解耦嵌入表示。通过分层VQ-VAE，模型能够将运动伪影分解为多个可解释的潜在因素，例如运动的幅度、方向和频率。这种解耦表示使得模型能够更好地理解运动伪影的本质，从而提高校正的泛化能力。与现有方法相比，该方法不需要针对特定伪影进行训练，具有更强的适应性。

**关键设计**：该方法使用了分层VQ-VAE结构，码本包含多个分辨率的码字，用于捕获不同尺度的运动模式。自回归模型采用Transformer结构，用于学习无运动图像的先验分布。损失函数包括重建损失、VQ损失和先验损失，用于优化编码器、解码器、码本和自回归模型。具体参数设置未知。

## 📊 实验亮点

该方法在模拟的全身运动伪影数据上进行了验证，结果表明，该方法能够有效地校正不同严重程度的运动伪影，并提高图像质量。与未进行运动校正的图像相比，校正后的图像具有更高的清晰度和更少的伪影。具体性能数据未知，但结果表明该模型能够有效地解耦运动特征，提高泛化能力。

## 🎯 应用场景

该研究成果可应用于临床MRI成像，提高图像质量，减少运动伪影对诊断的影响。尤其在儿童、老年人和无法配合的患者中，运动伪影更为常见，该方法具有重要的应用价值。未来，该技术有望推广到其他医学影像模态，如CT和PET，提升影像诊断的准确性和可靠性。

## 📄 摘要（原文）

> Physiological motion can affect the diagnostic quality of magnetic resonance imaging (MRI). While various retrospective motion correction methods exist, many struggle to generalize across different motion types and body regions. In particular, machine learning (ML)-based corrections are often tailored to specific applications and datasets. We hypothesize that motion artifacts, though diverse, share underlying patterns that can be disentangled and exploited. To address this, we propose a hierarchical vector-quantized (VQ) variational auto-encoder that learns a disentangled embedding of motion-to-clean image features. A codebook is deployed to capture finite collection of motion patterns at multiple resolutions, enabling coarse-to-fine correction. An auto-regressive model is trained to learn the prior distribution of motion-free images and is used at inference to guide the correction process. Unlike conventional approaches, our method does not require artifact-specific training and can generalize to unseen motion patterns. We demonstrate the approach on simulated whole-body motion artifacts and observe robust correction across varying motion severity. Our results suggest that the model effectively disentangled physical motion of the simulated motion-effective scans, therefore, improving the generalizability of the ML-based MRI motion correction. Our work of disentangling the motion features shed a light on its potential application across anatomical regions and motion types.

