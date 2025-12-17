---
layout: default
title: QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs
---

# QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.11696" target="_blank" class="toolbar-btn">arXiv: 2510.11696v1</a>
    <a href="https://arxiv.org/pdf/2510.11696.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11696v1" 
            onclick="toggleFavorite(this, '2510.11696v1', 'QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Wei Huang, Yi Ge, Shuai Yang, Yicheng Xiao, Huizi Mao, Yujun Lin, Hanrong Ye, Sifei Liu, Ka Chun Cheung, Hongxu Yin, Yao Lu, Xiaojuan Qi, Song Han, Yukang Chen

**分类**: cs.LG, cs.CL, cs.CV

**发布日期**: 2025-10-13

**备注**: Code is available at https://github.com/NVlabs/QeRL

---

## 💡 一句话要点

**QeRL：量化增强的LLM强化学习框架，提升效率并增强探索能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大型语言模型` `量化` `低秩适应` `模型压缩` `策略探索` `自适应噪声`

## 📋 核心要点

1. 现有LLM的强化学习训练资源消耗大，需要大量GPU内存和长时间的rollout，效率是主要瓶颈。
2. QeRL结合NVFP4量化和LoRA，加速rollout并降低内存占用，同时利用量化噪声增强探索。
3. 实验表明，QeRL加速rollout，降低内存需求，并在数学基准测试中达到或超过现有方法性能。

## 📝 摘要（中文）

本文提出了QeRL，一个用于大型语言模型（LLMs）的量化增强强化学习框架。强化学习对于提升LLMs的推理能力至关重要，但其资源消耗巨大，需要大量的GPU内存和较长的rollout时间。QeRL通过结合NVFP4量化和低秩适应（LoRA）来解决这些问题，从而加速强化学习的rollout阶段并降低内存开销。研究表明，量化噪声增加了策略熵，增强了探索能力，从而在强化学习期间能够发现更好的策略。为了进一步优化探索，QeRL引入了一种自适应量化噪声（AQN）机制，该机制在训练期间动态调整噪声。实验表明，QeRL在rollout阶段提供了超过1.5倍的加速。此外，这是第一个能够在单个H100 80GB GPU上对32B LLM进行强化学习训练的框架，同时提供了整体的强化学习训练加速。在7B模型上，它还实现了比16位LoRA和QLoRA更快的奖励增长和更高的最终准确率，同时在GSM8K（90.8%）和MATH 500（77.4%）等数学基准测试中与全参数微调的性能相匹配。这些结果确立了QeRL作为LLMs中强化学习训练的高效且有效的框架。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）强化学习训练过程中资源消耗过高的问题。现有的强化学习方法，尤其是应用于LLMs时，需要大量的GPU内存和较长的rollout时间，这限制了模型规模和训练效率。

**核心思路**：论文的核心思路是通过量化来降低内存占用和加速计算，同时利用量化过程引入的噪声来增强策略探索。通过结合NVFP4量化和低秩适应（LoRA），在保证性能的同时，显著降低资源需求。自适应量化噪声（AQN）机制进一步优化了探索过程。

**技术框架**：QeRL框架主要包含以下几个阶段：首先，使用NVFP4量化对LLM进行量化，降低内存占用。然后，结合LoRA进行参数高效的微调。在强化学习的rollout阶段，利用量化后的模型进行策略评估和样本生成。最后，使用自适应量化噪声（AQN）机制动态调整量化噪声，以优化探索过程。整个框架旨在在降低资源消耗的同时，提升强化学习的效率和性能。

**关键创新**：QeRL的关键创新在于将量化技术与强化学习相结合，并利用量化噪声来增强策略探索。传统的量化通常被视为一种降低模型大小和加速推理的手段，而QeRL则创新性地利用量化噪声来促进策略的多样性，从而避免陷入局部最优解。此外，自适应量化噪声（AQN）机制能够根据训练进度动态调整噪声水平，进一步优化探索过程。

**关键设计**：QeRL的关键设计包括：1) 使用NVFP4量化，在精度和效率之间取得平衡。2) 结合LoRA进行参数高效的微调，降低训练成本。3) 引入自适应量化噪声（AQN）机制，通过动态调整量化噪声的幅度来控制探索的程度。 AQN的具体实现细节（例如，如何根据训练进度调整噪声水平）在论文中可能包含更详细的描述，但摘要中未明确指出具体的公式或算法。

## 📊 实验亮点

QeRL在rollout阶段实现了超过1.5倍的加速，并且首次实现了在单个H100 80GB GPU上对32B LLM进行强化学习训练。在7B模型上，QeRL比16位LoRA和QLoRA实现了更快的奖励增长和更高的最终准确率，同时在GSM8K（90.8%）和MATH 500（77.4%）等数学基准测试中与全参数微调的性能相匹配。

## 🎯 应用场景

QeRL框架可广泛应用于需要强化学习训练的大型语言模型，例如对话系统、智能助手、游戏AI等。该方法降低了训练成本和资源需求，使得更大规模的模型和更复杂的任务成为可能。未来，QeRL可以进一步扩展到其他模型压缩技术和强化学习算法，为LLM的部署和应用带来更广阔的前景。

## 📄 摘要（原文）

> We propose QeRL, a Quantization-enhanced Reinforcement Learning framework for large language models (LLMs). While RL is essential for LLMs' reasoning capabilities, it is resource-intensive, requiring substantial GPU memory and long rollout durations. QeRL addresses these issues by combining NVFP4 quantization with Low-Rank Adaptation (LoRA), accelerating rollout phase of RL while reducing memory overhead. Beyond efficiency, our findings show that quantization noise increases policy entropy, enhancing exploration, and enabling the discovery of better strategies during RL. To further optimize exploration, QeRL introduces an Adaptive Quantization Noise (AQN) mechanism, which dynamically adjusts noise during training. Experiments demonstrate that QeRL delivers over 1.5 times speedup in the rollout phase. Moreover, this is the first framework to enable RL training of a 32B LLM on a single H100 80GB GPU, while delivering overall speedups for RL training. It also achieves faster reward growth and higher final accuracy than 16-bit LoRA and QLoRA, while matching the performance of full-parameter fine-tuning on mathematical benchmarks such as GSM8K (90.8%) and MATH 500 (77.4%) in the 7B model. These results establish QeRL as an efficient and effective framework for RL training in LLMs.

