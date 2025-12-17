---
layout: default
title: Physically Grounded Monocular Depth via Nanophotonic Wavefront Prompting
---

# Physically Grounded Monocular Depth via Nanophotonic Wavefront Prompting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2503.15770" class="toolbar-btn" target="_blank">📄 arXiv: 2503.15770</a>
  <a href="https://arxiv.org/pdf/2503.15770.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2503.15770" onclick="toggleFavorite(this, '2503.15770', 'Physically Grounded Monocular Depth via Nanophotonic Wavefront Prompting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bingxuan Li, Jiahao Wu, Yuan Xu, Zezheng Zhu, Yunxiang Zhang, Kenneth Chen, Yanqi Liang, Nanfang Yu, Qi Sun

**分类**: cs.AR, cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**利用纳米光子波前调控，实现物理可信的单目深度估计**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `单目深度估计` `超透镜` `波前调控` `纳米光子学` `深度学习` `物理约束` `光波传播模拟`

## 📋 核心要点

1. 深度学习模型缺乏物理深度线索，导致单目深度估计结果在尺度上存在不确定性。
2. 利用超透镜对光波进行调控，将深度信息编码到偏振光波前中，为深度估计提供物理约束。
3. 通过光波传播模拟器生成训练数据，并结合轻量级微调框架，实现准确的单目深度估计。

## 📝 摘要（中文）

深度基础模型在3D感知方面表现出强大的先验知识，但缺乏物理深度线索，导致度量尺度模糊。本文提出一种双折射超透镜——一种由亚波长像素组成的平面纳米光子透镜，厚度为700纳米，直径为3毫米——用于物理提示深度基础模型。在单次单目拍摄中，我们的超透镜将深度信息物理地嵌入到两个偏振光波前中，我们通过轻量级的提示和微调框架来解码这些信息，使深度基础模型与光学信号对齐。为了扩展训练数据，我们开发了一种光波传播模拟器，可以从RGB-D数据集中合成超透镜响应，并结合关键物理因素以最小化模拟到真实的差距。使用我们制造的二氧化钛超透镜进行的模拟和物理实验表明，与最先进的单目深度估计器相比，我们的方法能够实现准确且一致的度量深度。该研究表明，纳米光子波前形成为将深度基础模型植根于物理深度感知提供了一种有希望的桥梁。

## 🔬 方法详解

**问题定义**：单目深度估计依赖于深度学习模型学习场景的先验知识，但缺乏真实的物理深度线索，导致估计结果在绝对尺度上存在偏差。现有方法难以将物理世界的深度信息有效融入到深度学习模型中，限制了单目深度估计的精度和可靠性。

**核心思路**：利用超透镜对入射光波进行调制，将深度信息编码到不同偏振态的光波中。通过分析这些偏振光波，可以提取出场景的深度信息，从而为深度学习模型提供物理约束，解决尺度不确定性问题。这种方法将物理光学与深度学习相结合，实现了物理可信的单目深度估计。

**技术框架**：该方法主要包含三个阶段：1) 超透镜设计与制造：设计并制造具有特定双折射特性的超透镜，使其能够将深度信息编码到偏振光波中。2) 光波传播模拟：开发光波传播模拟器，用于生成大量带有深度信息的训练数据，并考虑了关键的物理因素，以减小模拟与真实数据之间的差距。3) 深度估计网络训练：利用模拟数据对深度学习模型进行预训练，然后使用真实数据进行微调，使模型能够准确地从偏振光波中提取深度信息。

**关键创新**：该方法的核心创新在于利用超透镜进行波前调控，将深度信息以物理的方式嵌入到光波中。与传统的基于学习的方法相比，该方法能够提供更强的物理约束，从而提高深度估计的精度和鲁棒性。此外，该方法还提出了一种光波传播模拟器，能够有效地生成训练数据，解决了真实数据获取困难的问题。

**关键设计**：超透镜采用二氧化钛材料，厚度为700纳米，直径为3毫米。光波传播模拟器考虑了材料的折射率、波长、偏振态等因素。深度估计网络采用轻量级的提示和微调框架，以适应超透镜编码的深度信息。损失函数包括深度损失和偏振损失，用于约束深度估计的精度和偏振信息的准确性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2503.15770/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2503.15770/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2503.15770/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在单目深度估计任务中取得了显著的性能提升。与最先进的单目深度估计器相比，该方法能够实现更准确和一致的度量深度。通过模拟和物理实验验证了该方法的有效性，并证明了纳米光子波前形成在深度感知方面的潜力。

## 🎯 应用场景

该研究成果可应用于机器人导航、增强现实、自动驾驶等领域。通过提供准确的单目深度估计，可以提高机器人对环境的感知能力，增强AR/VR应用的沉浸感，并提升自动驾驶系统的安全性。此外，该技术还可以应用于三维重建、虚拟现实等领域，具有广阔的应用前景。

## 📄 摘要（原文）

> Depth foundation models offer strong learned priors for 3D perception but lack physical depth cues, leading to ambiguities in metric scale. We introduce a birefringent metalens -- a planar nanophotonic lens composed of subwavelength pixels for wavefront shaping with a thickness of 700 nm and a diameter of 3 mm -- to physically prompt depth foundation models. In a single monocular shot, our metalens physically embeds depth information into two polarized optical wavefronts, which we decode through a lightweight prompting and fine-tuning framework that aligns depth foundation models with the optical signals. To scale the training data, we develop a light wave propagation simulator that synthesizes metalens responses from RGB-D datasets, incorporating key physical factors to minimize the sim-to-real gap. Simulated and physical experiments with our fabricated titanium-dioxide metalens demonstrate accurate and consistent metric depth over state-of-the-art monocular depth estimators. The research demonstrates that nanophotonic wavefront formation offers a promising bridge for grounding depth foundation models in physical depth sensing.

