---
layout: default
title: "StereoAdapter: Adapting Stereo Depth Estimation to Underwater Scenes"
---

# StereoAdapter: Adapting Stereo Depth Estimation to Underwater Scenes

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16415" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16415v1</a>
  <a href="https://arxiv.org/pdf/2509.16415.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16415v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16415v1', 'StereoAdapter: Adapting Stereo Depth Estimation to Underwater Scenes')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhengri Wu, Yiran Wang, Yu Wen, Zeyu Zhang, Biao Wu, Hao Tang

**分类**: cs.CV, cs.RO

**发布日期**: 2025-09-19

**🔗 代码/项目**: [GITHUB](https://github.com/AIGeeksGroup/StereoAdapter) | [PROJECT_PAGE](https://aigeeksgroup.github.io/StereoAdapter)

---

## 💡 一句话要点

**提出StereoAdapter以解决水下场景深度估计问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `水下深度估计` `自监督学习` `立体视觉` `LoRA适配` `机器人导航` `三维几何` `环境监测`

## 📋 核心要点

1. 现有水下立体深度估计方法在缺乏大量标注数据的情况下，难以高效适应水下环境，并且在融合单目和立体信息时存在尺度模糊问题。
2. 本文提出StereoAdapter框架，通过自监督学习结合LoRA适配的单目编码器与递归立体精细化模块，有效解决了上述问题。
3. 在TartanAir和SQUID基准测试中，StereoAdapter分别提升了6.11%和5.12%的性能，且在BlueROV2机器人上的实际部署验证了其鲁棒性。

## 📝 摘要（中文）

水下立体深度估计为机器人任务提供了准确的三维几何信息，如导航、检查和制图，利用低成本的被动相机提供度量深度，同时避免了单目方法的尺度模糊。然而，现有方法面临两个关键挑战：一是如何在缺乏大量标注数据的情况下高效地将大型视觉基础编码器适应水下领域，二是如何将全球一致但尺度模糊的单目先验与局部度量但光度脆弱的立体对应关系紧密融合。为了解决这些挑战，本文提出了StereoAdapter，一个参数高效的自监督框架，集成了LoRA适配的单目基础编码器和递归立体精细化模块。我们进一步引入动态LoRA适配以实现高效的秩选择，并在合成的UW-StereoDepth-40K数据集上进行预训练，以增强在多样化水下条件下的鲁棒性。综合评估显示，在TartanAir和SQUID基准测试上分别提升了6.11%和5.12%的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决水下场景中的立体深度估计问题，现有方法在缺乏标注数据的情况下难以有效适应水下环境，同时在融合单目和立体信息时存在尺度模糊的挑战。

**核心思路**：提出StereoAdapter框架，通过自监督学习的方式，将LoRA适配的单目基础编码器与递归立体精细化模块相结合，以实现高效的参数适应和深度估计。

**技术框架**：StereoAdapter的整体架构包括两个主要模块：LoRA适配的单目编码器和递归立体精细化模块。前者负责提取单目图像特征，后者则通过递归方式优化立体深度估计。

**关键创新**：本文的关键创新在于引入动态LoRA适配技术，实现高效的秩选择，并在合成数据集上进行预训练，从而增强了模型在多样化水下条件下的鲁棒性。与现有方法相比，StereoAdapter在参数效率和深度估计精度上具有显著优势。

**关键设计**：在模型设计中，采用了自监督损失函数以减少对标注数据的依赖，同时在网络结构上进行了优化，以提高特征提取和深度估计的精度。

## 📊 实验亮点

在综合评估中，StereoAdapter在TartanAir和SQUID基准测试上分别实现了6.11%和5.12%的性能提升，显示出其在水下深度估计中的优越性。此外，实际部署于BlueROV2机器人验证了其在复杂水下环境中的鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括水下机器人导航、环境监测、海洋探测等。通过提供准确的三维几何信息，StereoAdapter能够显著提升水下任务的效率和安全性，未来可能在海洋科学研究和资源开发等领域产生重要影响。

## 📄 摘要（原文）

> Underwater stereo depth estimation provides accurate 3D geometry for robotics tasks such as navigation, inspection, and mapping, offering metric depth from low-cost passive cameras while avoiding the scale ambiguity of monocular methods. However, existing approaches face two critical challenges: (i) parameter-efficiently adapting large vision foundation encoders to the underwater domain without extensive labeled data, and (ii) tightly fusing globally coherent but scale-ambiguous monocular priors with locally metric yet photometrically fragile stereo correspondences. To address these challenges, we propose StereoAdapter, a parameter-efficient self-supervised framework that integrates a LoRA-adapted monocular foundation encoder with a recurrent stereo refinement module. We further introduce dynamic LoRA adaptation for efficient rank selection and pre-training on the synthetic UW-StereoDepth-40K dataset to enhance robustness under diverse underwater conditions. Comprehensive evaluations on both simulated and real-world benchmarks show improvements of 6.11% on TartanAir and 5.12% on SQUID compared to state-of-the-art methods, while real-world deployment with the BlueROV2 robot further demonstrates the consistent robustness of our approach. Code: https://github.com/AIGeeksGroup/StereoAdapter. Website: https://aigeeksgroup.github.io/StereoAdapter.

