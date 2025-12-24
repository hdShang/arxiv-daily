---
layout: default
title: Memory as Resonance: A Biomimetic Architecture for Infinite Context Memory on Ergodic Phonetic Manifolds
---

# Memory as Resonance: A Biomimetic Architecture for Infinite Context Memory on Ergodic Phonetic Manifolds

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20245" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20245v1</a>
  <a href="https://arxiv.org/pdf/2512.20245.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20245v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20245v1', 'Memory as Resonance: A Biomimetic Architecture for Infinite Context Memory on Ergodic Phonetic Manifolds')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tarik Houichime, Abdelghani Souhar, Younes El Amrani

**分类**: cs.NE, cs.AI, cs.IR, cs.SC, cs.SE

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**提出基于遍历语音流形的共振记忆架构PTM，解决大语言模型无限上下文记忆问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长文本记忆` `遍历流形` `神经符号架构` `无理旋转矩阵` `信号共识` `大语言模型` `上下文学习`

## 📋 核心要点

1. 现有大语言模型受限于上下文窗口大小，无法有效处理长程依赖，面临遗忘和高延迟的挑战。
2. 论文提出语音轨迹记忆（PTM），将语言编码为遍历流形上的连续路径，实现高效压缩和快速检索。
3. 实验表明，PTM在长文本记忆方面实现了超过3000倍的压缩，并保持了较高的事实准确率（约92%）。

## 📝 摘要（中文）

当前大型语言模型的记忆受限于物理限制：随着学习的进行，模型容量逐渐耗尽。键-值状态的线性累积（O(N)）将上下文视为静态信息的仓库，最终迫使模型在遗忘和延迟之间做出选择。我们挑战了这种离散的正统观念，认为长期记忆不是存储项目，而是轨迹的持久性。我们引入了语音轨迹记忆（PTM），一种神经符号架构，它不是将语言编码为张量序列，而是编码为由无理旋转矩阵控制的遍历流形上的连续路径。通过将导航（不变的O(1)几何信号）与重构（概率生成行为）解耦，PTM实现了相对于密集缓存大于3000倍的压缩率。我们证明了检索成为一个共振过程：语音轨迹通过“信号共识”机制稳定模型，防止幻觉，确保高达约92%的事实准确性。虽然这种激进的抽象改变了生成纹理，但它解锁了独立于深度的即时访问延迟（约34毫秒）。我们的结果表明，无限上下文不需要无限的硅，而是需要将记忆视为作用于守恒的、不朽的物理信号的重构过程。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLM）在处理长上下文时面临着严重的挑战。传统的键值对存储方式导致内存需求随上下文长度线性增长（O(N)），这限制了模型能够处理的上下文长度，并导致检索延迟增加。此外，这种离散的存储方式将上下文视为静态信息的集合，忽略了语言的动态特性，容易导致模型产生幻觉。

**核心思路**：论文的核心思路是将长期记忆视为轨迹的持久性，而不是静态信息的存储。具体来说，论文将语言编码为遍历流形上的连续路径，利用无理旋转矩阵控制路径的演化。这种方法将导航（上下文定位）与重构（信息生成）解耦，从而实现高效的压缩和快速的检索。通过将上下文表示为连续的轨迹，模型可以更好地捕捉语言的动态特性，并减少幻觉的产生。

**技术框架**：PTM的核心框架包括以下几个主要模块：1) **语音编码器**：将输入的文本转换为语音特征表示。2) **遍历流形**：使用无理旋转矩阵构建一个高维的遍历流形，用于表示上下文轨迹。3) **轨迹生成器**：根据语音特征生成在遍历流形上的连续路径。4) **信号共识模块**：通过比较当前输入与历史轨迹，实现对模型的稳定，减少幻觉。5) **解码器**：根据遍历流形上的位置重构文本。

**关键创新**：PTM的关键创新在于将语言编码为遍历流形上的连续路径，并利用无理旋转矩阵控制路径的演化。这种方法实现了以下几个方面的优势：1) **高效压缩**：通过将上下文表示为连续的轨迹，PTM实现了远高于传统键值对存储的压缩率。2) **快速检索**：通过将导航与重构解耦，PTM实现了与上下文长度无关的快速检索。3) **减少幻觉**：通过信号共识机制，PTM可以有效地稳定模型，减少幻觉的产生。

**关键设计**：PTM的关键设计包括：1) **无理旋转矩阵**：使用无理旋转矩阵保证遍历流形的遍历性，确保模型可以访问到所有的上下文信息。2) **信号共识损失**：设计信号共识损失函数，鼓励模型生成与历史轨迹一致的输出，从而减少幻觉。3) **概率生成模型**：使用概率生成模型根据遍历流形上的位置重构文本，实现信息的解码。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20245v1/Images/torusv3.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20245v1/Images/max_drift-rotations-merged.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20245v1/Images/architecture.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

PTM在实验中表现出了显著的优势。相对于传统的密集缓存，PTM实现了超过3000倍的压缩率，同时保持了较低的检索延迟（约34毫秒）。此外，PTM通过信号共识机制，将事实准确率提高到约92%，显著减少了模型产生幻觉的可能性。这些结果表明，PTM是一种非常有前景的长文本记忆架构。

## 🎯 应用场景

PTM具有广泛的应用前景，例如：1) **长文本生成**：可以用于生成长篇小说、报告等。2) **对话系统**：可以用于构建具有长期记忆的对话系统。3) **信息检索**：可以用于在海量文本数据中进行快速检索。PTM的出现有望推动人工智能在长程依赖任务上的发展，并为构建更智能、更可靠的AI系统提供新的思路。

## 📄 摘要（原文）

> The memory of contemporary Large Language Models is bound by a physical paradox: as they learn, they fill up. The linear accumulation (O(N)) of Key-Value states treats context as a warehouse of static artifacts, eventually forcing a destructive choice between amnesia and latency. We challenge this discrete orthodoxy, proposing that long-term memory is not the storage of items, but the persistence of a trajectory. We introduce Phonetic Trajectory Memory (PTM), a neuro-symbolic architecture that encodes language not as a sequence of tensors, but as a continuous path on an ergodic manifold governed by irrational rotation matrices. By decoupling the navigation (an invariant O(1) geometric signal) from the reconstruction (a probabilistic generative act), PTM achieves a compression magnitude of greater than 3,000x relative to dense caches. We demonstrate that retrieval becomes a process of resonance: the phonetic trace stabilizes the model against hallucination via "Signal Consensus" mechanism, securing up to approximately 92% factual accuracy. While this aggressive abstraction alters generative texture, it unlocks immediate access latency (approximately 34ms) independent of depth. Our results suggest that infinite context does not require infinite silicon; it requires treating memory not as data to be stored, but as a reconstructive process acting on a conserved, undying physical signal.

