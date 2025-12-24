---
layout: default
title: "Insertion Language Models: Sequence Generation with Arbitrary-Position Insertions"
---

# Insertion Language Models: Sequence Generation with Arbitrary-Position Insertions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.05755" class="toolbar-btn" target="_blank">📄 arXiv: 2505.05755v3</a>
  <a href="https://arxiv.org/pdf/2505.05755.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.05755v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.05755v3', 'Insertion Language Models: Sequence Generation with Arbitrary-Position Insertions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dhruvesh Patel, Aishwarya Sahoo, Avinash Amballa, Tahira Naseem, Tim G. J. Rudner, Andrew McCallum

**分类**: cs.CL, cs.LG

**发布日期**: 2025-05-09 (更新: 2025-09-03)

**备注**: Additional related work. Code available at: https://dhruveshp.com/projects/ilm

---

## 💡 一句话要点

**提出插入语言模型以解决序列生成中的复杂约束问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `插入语言模型` `序列生成` `自回归模型` `掩蔽扩散模型` `自然语言处理` `文本生成` `依赖关系建模`

## 📋 核心要点

1. 现有的自回归模型在处理复杂约束和非顺序依赖的序列生成任务时存在局限性。
2. 本文提出插入语言模型（ILMs），通过逐个插入令牌的方式，能够在任意位置进行插入，从而更好地捕捉令牌之间的依赖关系。
3. 实验证明，ILMs在规划任务上超越了自回归模型和掩蔽扩散模型，并在无条件文本生成任务中表现出色，展现了更高的灵活性。

## 📝 摘要（中文）

自回归模型（ARMs）在序列生成任务中取得了显著成功，但在处理复杂约束或非顺序依赖的序列时表现不佳。虽然掩蔽扩散模型（MDMs）部分解决了这些问题，但同时解码多个令牌可能导致不连贯，并且无法处理未知数量的插入约束。本文提出插入语言模型（ILMs），能够在序列中任意位置插入令牌，通过逐个插入的方式，ILMs能够有效表示令牌之间的强依赖关系，并准确建模不遵循左到右顺序的序列。实验证明，ILMs在常见规划任务上优于ARMs和MDMs，并在无条件文本生成任务中与ARMs表现相当，同时在任意长度文本填充中提供了更大的灵活性。

## 🔬 方法详解

**问题定义**：本文旨在解决自回归模型在序列生成中无法有效处理复杂约束和非顺序依赖的问题。现有的掩蔽扩散模型在同时解码多个令牌时可能导致不连贯，且无法应对未知数量的插入约束。

**核心思路**：插入语言模型（ILMs）通过逐个插入令牌的方式，选择插入位置和词汇元素，能够有效捕捉令牌之间的强依赖关系，并支持任意顺序的生成。

**技术框架**：ILMs的整体架构包括一个特定的网络参数化设计，采用简单的去噪目标进行训练。模型通过逐步插入令牌，构建出完整的序列。

**关键创新**：ILMs的主要创新在于其能够在任意位置插入令牌，解决了传统模型在处理复杂序列时的局限性。这一设计使得模型能够灵活应对多样化的生成任务。

**关键设计**：ILMs的训练过程中采用了特定的损失函数和网络结构，确保模型能够有效学习插入过程中的依赖关系。具体的参数设置和网络架构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，插入语言模型（ILMs）在常见规划任务上显著超越了自回归模型和掩蔽扩散模型，具体表现为在多个任务中提高了生成的准确性和连贯性。此外，在无条件文本生成任务中，ILMs与自回归模型表现相当，同时在任意长度文本填充任务中展现出更大的灵活性。

## 🎯 应用场景

插入语言模型（ILMs）在文本生成、对话系统和自然语言处理等领域具有广泛的应用潜力。其灵活的插入机制能够满足多种复杂的生成需求，提升生成内容的质量和一致性。未来，ILMs有望在更复杂的生成任务中发挥重要作用，推动自然语言处理技术的发展。

## 📄 摘要（原文）

> Autoregressive models (ARMs), which predict subsequent tokens one-by-one ``from left to right,'' have achieved significant success across a wide range of sequence generation tasks. However, they struggle to accurately represent sequences that require satisfying sophisticated constraints or whose sequential dependencies are better addressed by out-of-order generation. Masked Diffusion Models (MDMs) address some of these limitations, but the process of unmasking multiple tokens simultaneously in MDMs can introduce incoherences, and MDMs cannot handle arbitrary infilling constraints when the number of tokens to be filled in is not known in advance. In this work, we introduce Insertion Language Models (ILMs), which learn to insert tokens at arbitrary positions in a sequence -- that is, they select jointly both the position and the vocabulary element to be inserted. By inserting tokens one at a time, ILMs can represent strong dependencies between tokens, and their ability to generate sequences in arbitrary order allows them to accurately model sequences where token dependencies do not follow a left-to-right sequential structure. To train ILMs, we propose a tailored network parameterization and use a simple denoising objective. Our empirical evaluation demonstrates that ILMs outperform both ARMs and MDMs on common planning tasks. Furthermore, we show that ILMs outperform MDMs and perform on par with ARMs in an unconditional text generation task while offering greater flexibility than MDMs in arbitrary-length text infilling. The code is available at: https://dhruveshp.com/projects/ilm .

