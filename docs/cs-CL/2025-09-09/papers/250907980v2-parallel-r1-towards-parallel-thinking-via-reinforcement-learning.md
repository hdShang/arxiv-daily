---
layout: default
title: "Parallel-R1: Towards Parallel Thinking via Reinforcement Learning"
---

# Parallel-R1: Towards Parallel Thinking via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07980" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07980v2</a>
  <a href="https://arxiv.org/pdf/2509.07980.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07980v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07980v2', 'Parallel-R1: Towards Parallel Thinking via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tong Zheng, Hongming Zhang, Wenhao Yu, Xiaoyang Wang, Runpeng Dai, Rui Liu, Huiwen Bao, Chengsong Huang, Heng Huang, Dong Yu

**分类**: cs.CL

**发布日期**: 2025-09-09 (更新: 2025-09-12)

**备注**: Project website: https://zhengkid.github.io/Parallel_R1.github.io/

**🔗 代码/项目**: [GITHUB](https://github.com/zhengkid/Parallel-R1)

---

## 💡 一句话要点

**提出Parallel-R1框架，通过强化学习赋能LLM并行思维能力，提升复杂推理任务性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `并行思维` `强化学习` `大型语言模型` `复杂推理` `课程学习`

## 📋 核心要点

1. 现有方法依赖于合成数据的监督微调，鼓励模仿而非探索和泛化，难以有效激活LLM的并行推理能力。
2. Parallel-R1采用强化学习框架，通过渐进式课程学习，先SFT灌输并行思维，再RL探索和泛化。
3. 实验表明，Parallel-R1能有效提升LLM在数学基准测试上的推理准确率，最高提升达42.9%。

## 📝 摘要（中文）

本文提出Parallel-R1，这是一个首个利用强化学习（RL）框架，使大型语言模型（LLM）具备并行思维能力，从而解决复杂现实世界推理任务的框架。该框架采用渐进式课程学习，显式地解决了RL训练并行思维时的冷启动问题。首先，在提示生成的、来自较简单任务的轨迹上使用监督微调（SFT），以灌输并行思维能力，然后过渡到RL，以探索和推广这种技能到更困难的问题上。在包括MATH、AMC23和AIME在内的各种数学基准测试上的实验表明，Parallel-R1成功地灌输了并行思维，与直接在具有挑战性的任务上使用RL训练的顺序思维模型相比，准确率提高了8.4%。进一步的分析表明，模型思维行为发生了明显转变：在早期阶段，它使用并行思维作为一种探索策略，而在后期阶段，它使用相同的功能进行多角度验证。最重要的是，我们验证了并行思维作为一种中期训练探索支架，其中这种临时探索阶段在RL之后解锁了更高的性能上限，在AIME25上比基线提高了42.9%。我们的模型、数据和代码将在https://github.com/zhengkid/Parallel-R1开源。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在复杂推理任务中，难以有效利用并行思维能力的问题。现有方法主要依赖于在合成数据上进行监督微调，这导致模型倾向于模仿教师数据，缺乏自主探索和泛化的能力，尤其是在面对真实世界中更具挑战性的问题时表现不佳。

**核心思路**：论文的核心思路是利用强化学习（RL）来训练LLM的并行思维能力。通过RL，模型可以在与环境的交互中自主探索不同的推理路径，并根据奖励信号学习如何更有效地利用并行思维来解决问题。为了解决RL训练中的冷启动问题，论文采用了一种渐进式课程学习策略，逐步增加任务的难度。

**技术框架**：Parallel-R1框架包含两个主要阶段：监督微调（SFT）阶段和强化学习（RL）阶段。在SFT阶段，模型首先在较简单的任务上进行训练，以学习基本的并行思维能力。这些训练数据通过提示工程生成。然后，在RL阶段，模型在更困难的任务上进行训练，通过与环境的交互来探索和优化其并行思维策略。框架使用奖励函数来鼓励模型进行有效的并行推理，并惩罚无效的推理路径。

**关键创新**：Parallel-R1的关键创新在于首次将强化学习应用于训练LLM的并行思维能力。与传统的监督微调方法相比，RL能够更好地鼓励模型进行自主探索和泛化，从而在更复杂的推理任务中取得更好的性能。此外，渐进式课程学习策略有效地解决了RL训练中的冷启动问题，使得模型能够逐步掌握并行思维的技能。

**关键设计**：Parallel-R1使用了一种基于策略梯度的强化学习算法，例如PPO。奖励函数的设计至关重要，它需要能够准确地评估模型并行推理的质量。例如，可以根据模型是否能够得出正确的答案，以及模型使用的推理路径的数量和质量来设计奖励函数。此外，模型的架构也需要支持并行推理，例如可以使用多个独立的解码器来生成不同的推理路径。

## 📊 实验亮点

实验结果表明，Parallel-R1在MATH、AMC23和AIME等数学基准测试上取得了显著的性能提升。与直接在困难任务上使用RL训练的顺序思维模型相比，Parallel-R1的准确率提高了8.4%。在AIME25测试中，Parallel-R1的性能比基线提高了42.9%，验证了并行思维作为中期训练探索支架的有效性。

## 🎯 应用场景

Parallel-R1框架具有广泛的应用前景，可用于提升LLM在数学、科学、编程等领域的推理能力。通过赋能LLM并行思维，可以使其更好地解决复杂问题，例如自动定理证明、代码生成和调试、科学发现等。该研究有望推动人工智能在各个领域的应用。

## 📄 摘要（原文）

> Parallel thinking has emerged as a novel approach for enhancing the reasoning capabilities of large language models (LLMs) by exploring multiple reasoning paths concurrently. However, activating such capabilities through training remains challenging, as existing methods predominantly rely on supervised fine-tuning (SFT) over synthetic data, which encourages teacher-forced imitation rather than exploration and generalization. Different from them, we propose \textbf{Parallel-R1}, the first reinforcement learning (RL) framework that enables parallel thinking behaviors for complex real-world reasoning tasks. Our framework employs a progressive curriculum that explicitly addresses the cold-start problem in training parallel thinking with RL. We first use SFT on prompt-generated trajectories from easier tasks to instill the parallel thinking ability, then transition to RL to explore and generalize this skill on harder problems. Experiments on various math benchmarks, including MATH, AMC23, and AIME, show that Parallel-R1 successfully instills parallel thinking, leading to 8.4% accuracy improvements over the sequential thinking model trained directly on challenging tasks with RL. Further analysis reveals a clear shift in the model's thinking behavior: at an early stage, it uses parallel thinking as an exploration strategy, while in a later stage, it uses the same capability for multi-perspective verification. Most significantly, we validate parallel thinking as a \textbf{mid-training exploration scaffold}, where this temporary exploratory phase unlocks a higher performance ceiling after RL, yielding a 42.9% improvement over the baseline on AIME25. Our model, data, and code will be open-source at https://github.com/zhengkid/Parallel-R1.

