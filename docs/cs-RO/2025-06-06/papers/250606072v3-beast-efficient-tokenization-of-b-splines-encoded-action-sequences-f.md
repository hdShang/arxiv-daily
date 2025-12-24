---
layout: default
title: "BEAST: Efficient Tokenization of B-Splines Encoded Action Sequences for Imitation Learning"
---

# BEAST: Efficient Tokenization of B-Splines Encoded Action Sequences for Imitation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06072" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06072v3</a>
  <a href="https://arxiv.org/pdf/2506.06072.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06072v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06072v3', 'BEAST: Efficient Tokenization of B-Splines Encoded Action Sequences for Imitation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongyi Zhou, Weiran Liao, Xi Huang, Yucheng Tang, Fabian Otto, Xiaogang Jia, Xinkai Jiang, Simon Hilber, Ge Li, Qian Wang, Ömer Erdinç Yağmurlu, Nils Blank, Moritz Reuss, Rudolf Lioutikov

**分类**: cs.RO, cs.LG

**发布日期**: 2025-06-06 (更新: 2025-10-24)

**备注**: Accepted by NeurIPS 2025

---

## 💡 一句话要点

**提出BEAST以高效编码B样条动作序列用于模仿学习**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `B样条` `动作序列` `模仿学习` `高效编码` `平滑轨迹` `深度学习` `机器人控制`

## 📋 核心要点

1. 现有的动作标记器在训练和推理过程中存在计算成本高、生成不平滑轨迹等问题。
2. BEAST通过B样条编码动作序列，避免了单独训练的需求，并确保生成统一长度的标记。
3. 实验结果显示，BEAST在166个模拟任务和8个真实任务中显著降低了计算成本，并生成了高频平滑控制信号。

## 📝 摘要（中文）

我们提出了B样条编码动作序列标记器（BEAST），这是一种新颖的动作标记器，利用B样条将动作序列编码为紧凑的离散或连续标记。与现有基于向量量化或字节对编码的动作标记器不同，BEAST无需单独的标记器训练，并且始终生成统一长度的标记，从而通过并行解码实现快速的动作序列生成。通过我们的B样条公式，BEAST自然确保生成平滑的轨迹，避免相邻段之间的不连续性。我们将BEAST与三种不同的模型架构集成进行广泛评估，结果表明BEAST显著降低了训练和推理的计算成本，并且在连续控制任务中可靠地生成平滑的高频控制信号，同时在任务成功率上与最先进的方法相比保持竞争力。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有动作标记器在训练和推理过程中的高计算成本及生成轨迹不平滑的问题。现有方法如向量量化和字节对编码存在需要单独训练和生成不一致长度标记的缺陷。

**核心思路**：BEAST的核心思路是利用B样条对动作序列进行编码，生成离散或连续的标记。通过这种方式，BEAST能够在不需要额外训练的情况下，快速生成统一长度的标记，并确保生成的轨迹平滑。

**技术框架**：BEAST的整体架构包括三个主要模块：动作序列的B样条编码、标记生成和解码。首先，输入的动作序列通过B样条进行编码，生成紧凑的标记；然后，这些标记被输入到不同的模型架构中进行解码。

**关键创新**：BEAST的主要创新在于其无需单独训练的标记生成机制和确保生成平滑轨迹的能力。这与现有方法的本质区别在于，BEAST能够在保持高效性的同时，避免了生成过程中的不连续性。

**关键设计**：在设计上，BEAST采用了B样条的数学特性，确保生成的标记在时间上是连续的。此外，模型的损失函数设计考虑了生成轨迹的平滑性，以提高控制信号的质量。

## 📊 实验亮点

实验结果表明，BEAST在166个模拟任务和8个真实任务中，训练和推理的计算成本显著降低，同时生成的高频控制信号在连续控制任务中表现出色。与最先进的方法相比，BEAST在任务成功率上保持了竞争力，展示了其优越的性能。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、自动驾驶和人机交互等场景。BEAST的高效编码和生成能力可以显著提升模仿学习系统的性能，降低计算资源消耗，推动智能系统在复杂任务中的应用。未来，BEAST可能会与更多的深度学习模型结合，进一步拓展其应用范围。

## 📄 摘要（原文）

> We present the B-spline Encoded Action Sequence Tokenizer (BEAST), a novel action tokenizer that encodes action sequences into compact discrete or continuous tokens using B-splines. In contrast to existing action tokenizers based on vector quantization or byte pair encoding, BEAST requires no separate tokenizer training and consistently produces tokens of uniform length, enabling fast action sequence generation via parallel decoding. Leveraging our B-spline formulation, BEAST inherently ensures generating smooth trajectories without discontinuities between adjacent segments. We extensively evaluate BEAST by integrating it with three distinct model architectures: a Variational Autoencoder (VAE) with continuous tokens, a decoder-only Transformer with discrete tokens, and Florence-2, a pretrained Vision-Language Model with an encoder-decoder architecture, demonstrating BEAST's compatibility and scalability with large pretrained models. We evaluate BEAST across three established benchmarks consisting of 166 simulated tasks and on three distinct robot settings with a total of 8 real-world tasks. Experimental results demonstrate that BEAST (i) significantly reduces both training and inference computational costs, and (ii) consistently generates smooth, high-frequency control signals suitable for continuous control tasks while (iii) reliably achieves competitive task success rates compared to state-of-the-art methods.

