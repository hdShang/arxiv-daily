---
layout: default
title: "MiMo: Unlocking the Reasoning Potential of Language Model -- From Pretraining to Posttraining"
---

# MiMo: Unlocking the Reasoning Potential of Language Model -- From Pretraining to Posttraining

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07608" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07608v2</a>
  <a href="https://arxiv.org/pdf/2505.07608.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07608v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07608v2', 'MiMo: Unlocking the Reasoning Potential of Language Model -- From Pretraining to Posttraining')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: LLM-Core Xiaomi, :, Bingquan Xia, Bowen Shen, Cici, Dawei Zhu, Di Zhang, Gang Wang, Hailin Zhang, Huaqiu Liu, Jiebao Xiao, Jinhao Dong, Liang Zhao, Peidian Li, Peng Wang, Shihua Yu, Shimao Chen, Weikun Wang, Wenhan Ma, Xiangwei Deng, Yi Huang, Yifan Song, Zihan Jiang, Bowen Ye, Can Cai, Chenhong He, Dong Zhang, Duo Zhang, Guoan Wang, Hao Tian, Haochen Zhao, Heng Qu, Hongshen Xu, Jun Shi, Kainan Bao, Kai Fang, Kang Zhou, Kangyang Zhou, Lei Li, Menghang Zhu, Nuo Chen, Qiantong Wang, Shaohui Liu, Shicheng Li, Shuhao Gu, Shuhuai Ren, Shuo Liu, Sirui Deng, Weiji Zhuang, Weiwei Lv, Wenyu Yang, Xin Zhang, Xing Yong, Xing Zhang, Xingchen Song, Xinzhe Xu, Xu Wang, Yihan Yan, Yu Tu, Yuanyuan Tian, Yudong Wang, Yue Yu, Zhenru Lin, Zhichao Song, Zihao Yue

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-12 (更新: 2025-06-05)

**🔗 代码/项目**: [GITHUB](https://github.com/xiaomimimo/MiMo)

---

## 💡 一句话要点

**提出MiMo-7B以增强语言模型的推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `推理能力` `强化学习` `数据预处理` `多标记预测` `数学问题` `编程问题` `模型优化`

## 📋 核心要点

1. 现有语言模型在推理任务上表现不足，尤其是在复杂的数学和编程问题上。
2. 论文提出了MiMo-7B，通过改进数据预处理和引入多标记预测目标，增强模型的推理能力。
3. 实验结果显示，MiMo-7B-Base在推理能力上超越了更大规模的32B模型，最终模型在多项任务中表现优异。

## 📝 摘要（中文）

我们提出了MiMo-7B，这是一个专为推理任务设计的大型语言模型，通过优化预训练和后训练阶段来提升其推理潜力。在预训练阶段，我们改进了数据预处理流程，并采用三阶段数据混合策略，以增强基础模型的推理能力。MiMo-7B-Base在250万亿个标记上进行预训练，并引入了多标记预测目标以提高性能和加速推理速度。在后训练阶段，我们策划了一个包含13万个可验证的数学和编程问题的数据集，结合测试难度驱动的代码奖励机制，以缓解稀疏奖励问题，并采用战略性数据重采样来稳定训练。广泛评估表明，MiMo-7B-Base在推理潜力上表现出色，甚至超越了更大的32B模型。最终的RL调优模型MiMo-7B-RL在数学、代码和一般推理任务上表现优异，超过了OpenAI的o1-mini。模型检查点可在https://github.com/xiaomimimo/MiMo获取。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有语言模型在推理任务中的不足，尤其是在处理复杂数学和编程问题时的表现不佳。现有方法往往面临数据稀疏和推理能力不足的问题。

**核心思路**：论文的核心思路是通过优化预训练和后训练阶段，提升模型的推理潜力。具体而言，采用三阶段数据混合策略和多标记预测目标，以增强模型的学习能力和推理速度。

**技术框架**：整体架构包括预训练和后训练两个主要阶段。在预训练阶段，模型在25万亿个标记上进行训练，并通过改进的数据预处理流程提升基础模型的性能。在后训练阶段，使用130K的数学和编程问题数据集进行强化学习，结合测试难度驱动的奖励机制。

**关键创新**：最重要的技术创新点在于引入了多标记预测目标和测试难度驱动的奖励机制，这些设计有效缓解了稀疏奖励问题，并提升了模型的推理能力。与现有方法相比，MiMo-7B在推理任务上展现出更强的能力。

**关键设计**：在模型设计中，采用了三阶段数据混合策略，并在后训练中实施了战略性数据重采样，以确保训练的稳定性。此外，模型的损失函数和奖励机制经过精心设计，以优化推理性能。

## 📊 实验亮点

实验结果显示，MiMo-7B-Base在推理能力上超越了更大规模的32B模型，最终的RL调优模型MiMo-7B-RL在数学、代码和一般推理任务上表现优异，超过了OpenAI的o1-mini，展现了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括教育、编程辅助、科学计算等，能够为用户提供更高效的推理和问题解决能力。未来，MiMo-7B有望在更广泛的推理任务中发挥重要作用，推动智能助手和自动化系统的发展。

## 📄 摘要（原文）

> We present MiMo-7B, a large language model born for reasoning tasks, with optimization across both pre-training and post-training stages. During pre-training, we enhance the data preprocessing pipeline and employ a three-stage data mixing strategy to strengthen the base model's reasoning potential. MiMo-7B-Base is pre-trained on 25 trillion tokens, with additional Multi-Token Prediction objective for enhanced performance and accelerated inference speed. During post-training, we curate a dataset of 130K verifiable mathematics and programming problems for reinforcement learning, integrating a test-difficulty-driven code-reward scheme to alleviate sparse-reward issues and employing strategic data resampling to stabilize training. Extensive evaluations show that MiMo-7B-Base possesses exceptional reasoning potential, outperforming even much larger 32B models. The final RL-tuned model, MiMo-7B-RL, achieves superior performance on mathematics, code and general reasoning tasks, surpassing the performance of OpenAI o1-mini. The model checkpoints are available at https://github.com/xiaomimimo/MiMo.

