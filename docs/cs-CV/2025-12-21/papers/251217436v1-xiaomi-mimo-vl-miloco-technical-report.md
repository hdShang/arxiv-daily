---
layout: default
title: Xiaomi MiMo-VL-Miloco Technical Report
---

# Xiaomi MiMo-VL-Miloco Technical Report

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17436" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17436v1</a>
  <a href="https://arxiv.org/pdf/2512.17436.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17436v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17436v1', 'Xiaomi MiMo-VL-Miloco Technical Report')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaze Li, Jingyang Chen, Yuxun Qu, Jianzhong Ju, Zhenbo Luo, Jian Luan, Shijie Xu, Zhenru Lin, Junyou Zhu, Boshen Xu, Wenhui Tan, Pei Fu

**分类**: cs.CV

**发布日期**: 2025-12-19

**🔗 代码/项目**: [GITHUB](https://github.com/XiaoMi/xiaomi-mimo-vl-miloco)

---

## 💡 一句话要点

**提出MiMo-VL-Miloco以解决智能家居场景理解问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `智能家居` `多模态理解` `视觉-语言模型` `强化学习` `手势识别` `家庭场景` `数据高效学习`

## 📋 核心要点

1. 现有的多模态模型在智能家居场景理解方面表现不足，尤其是在手势识别和活动理解上存在局限性。
2. 论文提出了一种基于MiMo-VL-7B的两阶段训练流程，结合了监督微调和强化学习，以提升模型在家庭场景中的表现。
3. 实验结果显示，MiMo-VL-Miloco-7B在多个基准测试中超越了现有的强基线，特别是在家庭场景理解和多模态推理任务上取得了显著提升。

## 📝 摘要（中文）

我们开源了MiMo-VL-Miloco-7B及其量化变体MiMo-VL-Miloco-7B-GGUF，这是一对专注于家庭场景的视觉-语言模型，在家庭场景理解和多模态推理方面表现优异。基于MiMo-VL-7B骨干网络，MiMo-VL-Miloco-7B专为智能家居环境设计，在手势识别和常见家庭场景理解上取得了领先的F1分数，同时在视频基准（如Video-MME、Video-MMMU和Charades-STA）和语言理解基准（如MMMU-Pro和MMLU-Pro）上也表现出一致的提升。实验结果表明，MiMo-VL-Miloco-7B在家庭场景理解和多个多模态推理基准上超越了强大的闭源和开源基线。我们设计了一个结合监督微调和基于组相对策略优化的强化学习的两阶段训练流程，利用高效的多领域数据，进一步引入链式思维监督和基于令牌预算的推理，使模型能够以数据高效的方式学习知识，同时高效地进行推理。

## 🔬 方法详解

**问题定义**：本论文旨在解决智能家居环境中的多模态理解问题，现有方法在手势识别和家庭场景理解方面存在性能不足，难以满足实际应用需求。

**核心思路**：提出的MiMo-VL-Miloco-7B模型通过结合监督学习和强化学习的两阶段训练流程，旨在提升模型在特定家庭场景中的理解能力，同时保持一定的通用性。

**技术框架**：整体架构包括两个主要阶段：首先进行监督微调，随后通过基于组相对策略优化的强化学习进行进一步训练。模型还引入了链式思维监督和令牌预算意识的推理机制，以提高学习效率和推理能力。

**关键创新**：最重要的创新点在于将强化学习与监督学习相结合，形成了一个高效的训练流程，能够在家庭场景中进行针对性训练，同时提升文本推理能力。

**关键设计**：模型设计中采用了多领域数据集进行训练，损失函数和网络结构经过精心调整，以确保在家庭场景理解和多模态推理任务中取得最佳性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17436v1/figure/radar.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17436v1/x1.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，MiMo-VL-Miloco-7B在家庭场景理解和多模态推理基准上超越了多个强基线，特别是在手势识别任务中取得了领先的F1分数，并在视频理解基准上也显示出一致的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括智能家居助手、家庭监控系统和人机交互界面等。通过提升模型在家庭场景中的理解能力，可以为用户提供更为智能和个性化的服务，未来可能在智能家居行业产生深远影响。

## 📄 摘要（原文）

> We open-source \textbf{MiMo-VL-Miloco-7B} and its quantized variant \textbf{MiMo-VL-Miloco-7B-GGUF}, a pair of home-centric vision-language models that achieve strong performance on both home-scenario understanding and general multimodal reasoning. Built on the MiMo-VL-7B backbone, MiMo-VL-Miloco-7B is specialized for smart-home environments, attaining leading F1 scores on gesture recognition and common home-scenario understanding, while also delivering consistent gains across video benchmarks such as Video-MME, Video-MMMU, and Charades-STA, as well as language understanding benchmarks including MMMU-Pro and MMLU-Pro. In our experiments, MiMo-VL-Miloco-7B outperforms strong closed-source and open-source baselines on home-scenario understanding and several multimodal reasoning benchmarks. To balance specialization and generality, we design a two-stage training pipeline that combines supervised fine-tuning with reinforcement learning based on Group Relative Policy Optimization, leveraging efficient multi-domain data. We further incorporate chain-of-thought supervision and token-budget-aware reasoning, enabling the model to learn knowledge in a data-efficient manner while also performing reasoning efficiently. Our analysis shows that targeted home-scenario training not only enhances activity and gesture understanding, but also improves text-only reasoning with only modest trade-offs on document-centric tasks. Model checkpoints, quantized GGUF weights, and our home-scenario evaluation toolkit are publicly available at \href{https://github.com/XiaoMi/xiaomi-mimo-vl-miloco}{https://github.com/XiaoMi/xiaomi-mimo-vl-miloco} to support research and deployment in real-world smart-home applications.

