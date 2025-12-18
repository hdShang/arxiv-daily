---
layout: default
title: Actial: Activate Spatial Reasoning Ability of Multimodal Large Language Models
---

# Actial: Activate Spatial Reasoning Ability of Multimodal Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.01618" class="toolbar-btn" target="_blank">📄 arXiv: 2511.01618v1</a>
  <a href="https://arxiv.org/pdf/2511.01618.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.01618v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.01618v1', 'Actial: Activate Spatial Reasoning Ability of Multimodal Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoyu Zhan, Wenxuan Huang, Hao Sun, Xinyu Fu, Changfeng Ma, Shaosheng Cao, Bohan Jia, Shaohui Lin, Zhenfei Yin, Lei Bai, Wanli Ouyang, Yuanqi Li, Jie Guo, Yanwen Guo

**分类**: cs.CV, cs.CL

**发布日期**: 2025-11-03

---

## 💡 一句话要点

**Actial：通过视角学习激活多模态大语言模型的空间推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `多模态大语言模型` `空间推理` `视角学习` `强化学习` `数据集` `跨视角一致性` `3D场景理解`

## 📋 核心要点

1. 现有MLLM在3D推理中缺乏有效的空间信息捕捉，尤其在跨视角一致性方面存在挑战。
2. 提出视角学习任务和Viewpoint-100K数据集，通过两阶段微调策略提升空间推理能力。
3. 实验表明，该方法显著激活MLLM的空间推理能力，提升了域内和域外推理任务的性能。

## 📝 摘要（中文）

多模态大语言模型(MLLM)在2D视觉理解方面取得了显著进展，激发了人们将其应用于复杂3D推理任务的兴趣。然而，这些模型是否能有效捕捉到稳健的真实世界性能所需的详细空间信息，尤其是在精确3D推理的关键要求——跨视角一致性方面，仍然不清楚。考虑到这个问题，我们引入了视角学习，这是一项旨在评估和提高MLLM空间推理能力的任务。我们提出了Viewpoint-100K数据集，包含10万个以对象为中心的图像对，具有不同的视角和相应的问答对。我们的方法采用两阶段微调策略：首先，通过在Viewpoint-100K上进行监督微调(SFT)，将基础知识注入到基线MLLM中，从而在多个任务中获得显著改进；其次，通过在更广泛的问题集上使用群体相对策略优化(GRPO)算法进行强化学习，增强泛化能力。此外，我们引入了一种混合冷启动初始化方法，旨在同时学习视角表示并保持连贯的推理思维。实验结果表明，我们的方法显著激活了MLLM的空间推理能力，提高了在域内和域外推理任务中的性能。我们的发现强调了在MLLM中发展基础空间技能的价值，支持机器人、自主系统和3D场景理解方面的未来进展。

## 🔬 方法详解

**问题定义**：现有的多模态大语言模型在处理需要精细空间推理的任务时表现不足，尤其是在理解不同视角下的物体关系和保持跨视角一致性方面存在困难。这限制了它们在机器人、自动驾驶等需要精确3D场景理解领域的应用。现有方法难以有效捕捉和利用图像中的空间信息，导致推理结果不准确。

**核心思路**：论文的核心思路是通过“视角学习”来提升MLLM的空间推理能力。具体而言，通过构建包含大量不同视角图像对的数据集，并设计相应的问答任务，让模型学习从不同视角观察同一物体时应该具备的理解能力。这种方法旨在让模型能够更好地理解和推理3D空间中的物体关系。

**技术框架**：整体框架包含两个主要阶段：1) 监督微调(SFT)：在Viewpoint-100K数据集上，使用监督学习的方式对MLLM进行微调，注入基础的空间知识。2) 强化学习：使用群体相对策略优化(GRPO)算法，在更广泛的问题集上进行强化学习，进一步提升模型的泛化能力。此外，还使用了混合冷启动初始化方法，以同时学习视角表示并保持推理连贯性。

**关键创新**：论文的关键创新在于提出了“视角学习”这一概念，并设计了相应的Viewpoint-100K数据集和两阶段微调策略。通过这种方式，有效地激活了MLLM的空间推理能力。混合冷启动初始化方法也是一个创新点，它能够同时学习视角表示并保持推理的连贯性。

**关键设计**：Viewpoint-100K数据集包含10万个以对象为中心的图像对，每个图像对包含不同视角的同一物体图像，并配有相应的问答对。两阶段微调策略中，SFT阶段使用交叉熵损失函数，GRPO阶段使用强化学习奖励函数。混合冷启动初始化方法的具体实现细节未知。

## 📊 实验亮点

实验结果表明，提出的方法显著提升了MLLM在空间推理任务上的性能。在Viewpoint-100K数据集上，性能提升显著。同时，该方法在域外推理任务上也表现出良好的泛化能力，证明了其有效性。具体的性能数据和提升幅度在论文中进行了详细的展示。

## 🎯 应用场景

该研究成果可广泛应用于机器人、自动驾驶、3D场景理解等领域。通过提升MLLM的空间推理能力，可以使机器人更好地理解周围环境，从而实现更智能的导航和操作。在自动驾驶领域，可以提高车辆对复杂交通场景的理解和判断能力，从而提升安全性。此外，该技术还可以应用于虚拟现实、增强现实等领域，提供更逼真的用户体验。

## 📄 摘要（原文）

> Recent advances in Multimodal Large Language Models (MLLMs) have significantly improved 2D visual understanding, prompting interest in their application to complex 3D reasoning tasks. However, it remains unclear whether these models can effectively capture the detailed spatial information required for robust real-world performance, especially cross-view consistency, a key requirement for accurate 3D reasoning. Considering this issue, we introduce Viewpoint Learning, a task designed to evaluate and improve the spatial reasoning capabilities of MLLMs. We present the Viewpoint-100K dataset, consisting of 100K object-centric image pairs with diverse viewpoints and corresponding question-answer pairs. Our approach employs a two-stage fine-tuning strategy: first, foundational knowledge is injected to the baseline MLLM via Supervised Fine-Tuning (SFT) on Viewpoint-100K, resulting in significant improvements across multiple tasks; second, generalization is enhanced through Reinforcement Learning using the Group Relative Policy Optimization (GRPO) algorithm on a broader set of questions. Additionally, we introduce a hybrid cold-start initialization method designed to simultaneously learn viewpoint representations and maintain coherent reasoning thinking. Experimental results show that our approach significantly activates the spatial reasoning ability of MLLM, improving performance on both in-domain and out-of-domain reasoning tasks. Our findings highlight the value of developing foundational spatial skills in MLLMs, supporting future progress in robotics, autonomous systems, and 3D scene understanding.

