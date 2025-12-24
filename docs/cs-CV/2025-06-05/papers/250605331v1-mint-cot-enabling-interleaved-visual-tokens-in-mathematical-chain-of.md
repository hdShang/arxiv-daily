---
layout: default
title: "MINT-CoT: Enabling Interleaved Visual Tokens in Mathematical Chain-of-Thought Reasoning"
---

# MINT-CoT: Enabling Interleaved Visual Tokens in Mathematical Chain-of-Thought Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05331" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05331v1</a>
  <a href="https://arxiv.org/pdf/2506.05331.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05331v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05331v1', 'MINT-CoT: Enabling Interleaved Visual Tokens in Mathematical Chain-of-Thought Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinyan Chen, Renrui Zhang, Dongzhi Jiang, Aojun Zhou, Shilin Yan, Weifeng Lin, Hongsheng Li

**分类**: cs.CV

**发布日期**: 2025-06-05

**备注**: Code is released at https://github.com/xinyan-cxy/MINT-CoT

**🔗 代码/项目**: [GITHUB](https://github.com/xinyan-cxy/MINT-CoT)

---

## 💡 一句话要点

**提出MINT-CoT以解决多模态数学推理中的视觉信号整合问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数学推理` `多模态学习` `视觉信号整合` `链式思维` `深度学习`

## 📋 核心要点

1. 现有方法在多模态数学推理中面临三大挑战，包括对粗糙图像区域的依赖、视觉编码器对数学内容的感知能力有限，以及对外部视觉修改能力的依赖。
2. 本文提出MINT-CoT，通过引入数学交织令牌，动态选择与推理步骤相关的视觉令牌，从而实现文本推理与视觉信号的有效交织。
3. 实验结果显示，MINT-CoT-7B模型在MathVista、GeoQA和MMStar等基准上分别提升了34.08%、28.78%和23.2%的性能，验证了方法的有效性。

## 📝 摘要（中文）

链式思维（CoT）在大型语言模型（LLMs）中显著增强了数学推理能力，但在多模态领域的扩展仍面临挑战。现有方法要么采用类似文本的推理方式处理图像输入，要么试图将视觉信号与数学CoT交织，但存在依赖粗糙的图像区域、视觉编码器对数学内容感知有限以及依赖外部能力进行视觉修改等三大关键限制。本文提出MINT-CoT，引入数学交织令牌以实现视觉推理，动态选择数学图形中的视觉区域，并构建包含54K数学问题的MINT-CoT数据集，支持逐步训练策略。实验结果表明，MINT-CoT-7B模型在多个基准上显著优于基线模型。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态数学推理中视觉信号整合不足的问题。现有方法依赖于粗糙的图像区域，导致对数学内容的理解和推理能力受限。

**核心思路**：MINT-CoT的核心思路是通过引入数学交织令牌，动态选择与推理步骤相关的视觉区域，从而实现文本与视觉信息的有效交织。这种设计旨在提高模型对数学问题的理解和解决能力。

**技术框架**：MINT-CoT的整体架构包括三个主要阶段：文本仅CoT的监督微调（SFT）、交织CoT的SFT，以及交织CoT的强化学习（RL）。每个阶段逐步增强模型的推理能力和视觉整合能力。

**关键创新**：MINT-CoT的主要创新在于引入了数学交织令牌，使得模型能够动态选择任意形状的视觉区域，与文本推理步骤相结合。这一方法与现有依赖固定形状区域的技术有本质区别。

**关键设计**：在模型训练中，采用了严格的数据生成管道，构建了包含54K数学问题的数据集，确保每个推理步骤与视觉区域在令牌级别上对齐。此外，训练过程中使用了多种损失函数和优化策略，以提升模型的性能。

## 📊 实验亮点

实验结果显示，MINT-CoT-7B模型在MathVista、GeoQA和MMStar基准上分别提升了34.08%、28.78%和23.2%的性能，显著优于现有基线模型，验证了该方法在多模态数学推理中的有效性。

## 🎯 应用场景

MINT-CoT的研究成果在教育、智能辅导、以及数学问题求解等领域具有广泛的应用潜力。通过有效整合视觉信息与文本推理，该方法能够帮助学生更好地理解数学概念，提升学习效果，并为未来的智能教育系统奠定基础。

## 📄 摘要（原文）

> Chain-of-Thought (CoT) has widely enhanced mathematical reasoning in Large Language Models (LLMs), but it still remains challenging for extending it to multimodal domains. Existing works either adopt a similar textual reasoning for image input, or seek to interleave visual signals into mathematical CoT. However, they face three key limitations for math problem-solving: reliance on coarse-grained box-shaped image regions, limited perception of vision encoders on math content, and dependence on external capabilities for visual modification. In this paper, we propose MINT-CoT, introducing Mathematical INterleaved Tokens for Chain-of-Thought visual reasoning. MINT-CoT adaptively interleaves relevant visual tokens into textual reasoning steps via an Interleave Token, which dynamically selects visual regions of any shapes within math figures. To empower this capability, we construct the MINT-CoT dataset, containing 54K mathematical problems aligning each reasoning step with visual regions at the token level, accompanied by a rigorous data generation pipeline. We further present a three-stage MINT-CoT training strategy, progressively combining text-only CoT SFT, interleaved CoT SFT, and interleaved CoT RL, which derives our MINT-CoT-7B model. Extensive experiments demonstrate the effectiveness of our method for effective visual interleaved reasoning in mathematical domains, where MINT-CoT-7B outperforms the baseline model by +34.08% on MathVista, +28.78% on GeoQA, and +23.2% on MMStar, respectively. Our code and data are available at https://github.com/xinyan-cxy/MINT-CoT

