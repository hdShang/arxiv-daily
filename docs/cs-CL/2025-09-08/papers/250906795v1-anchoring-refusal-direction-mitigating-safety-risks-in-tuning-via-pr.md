---
layout: default
title: "Anchoring Refusal Direction: Mitigating Safety Risks in Tuning via Projection Constraint"
---

# Anchoring Refusal Direction: Mitigating Safety Risks in Tuning via Projection Constraint

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.06795" class="toolbar-btn" target="_blank">📄 arXiv: 2509.06795v1</a>
  <a href="https://arxiv.org/pdf/2509.06795.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.06795v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.06795v1', 'Anchoring Refusal Direction: Mitigating Safety Risks in Tuning via Projection Constraint')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanrui Du, Fenglei Fan, Sendong Zhao, Jiawei Cao, Qika Lin, Kai He, Ting Liu, Bing Qin, Mengling Feng

**分类**: cs.CL

**发布日期**: 2025-09-08

---

## 💡 一句话要点

**提出ProCon方法，通过投影约束缓解指令微调中大语言模型的安全性风险。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `指令微调` `安全性` `拒绝方向` `投影约束` `模型安全` `可解释性` `对抗训练`

## 📋 核心要点

1. 指令微调虽提升大语言模型能力，但会显著降低其拒绝恶意指令的安全性，核心问题在于训练过程中拒绝方向（r-direction）的漂移。
2. ProCon方法通过引入投影约束损失项，正则化训练样本隐藏状态在拒绝方向上的投影幅度，从而抑制r-direction的漂移。
3. 实验表明，ProCon方法在降低安全风险的同时，保持了任务性能，并且优于现有基线方法，有助于稳定训练过程中的r-direction。

## 📝 摘要（中文）

指令微调(IFT)已被广泛采用作为一种有效的后训练策略，以增强大型语言模型(LLM)的各种能力。然而，先前的研究表明，IFT会显著损害LLM的安全性，特别是它们拒绝恶意指令的能力，从而引起重大关注。最近对LLM内部机制的研究已经确定了隐藏状态中的拒绝方向(r-direction)，它在控制拒绝行为中起着关键作用。基于这一洞察，我们的研究表明，r-direction在训练期间容易漂移，我们将其识别为相关安全风险的原因之一。为了减轻这种漂移，我们提出的ProCon方法引入了一个投影约束损失项，该损失项正则化每个训练样本的隐藏状态在r-direction上的投影幅度。我们的初步分析表明，应用适当的约束可以有效地减轻拒绝方向漂移和相关的安全风险，但仍然受到整体性能障碍的限制。为了克服这一障碍，根据我们对早期急剧漂移的观察和数据驱动的视角，我们引入了一种warm-up策略，该策略强调早期强约束并扩大数据分布以加强约束信号，从而产生增强的ProCon方法。在各种数据集、场景和LLM下的实验结果表明，我们的方法可以显著降低IFT带来的安全风险，同时保持任务性能的提升。即使与强大的基线相比，我们的方法也能始终如一地提供卓越的整体性能。至关重要的是，我们的分析表明，ProCon有助于在训练期间稳定r-direction，同时这种对LLM内部机制的基于可解释性的探索为未来的安全研究奠定了坚实的基础。

## 🔬 方法详解

**问题定义**：指令微调（IFT）在提升大语言模型（LLM）性能的同时，会降低其安全性，特别是拒绝恶意指令的能力。现有方法缺乏对LLM内部机制的深入理解，导致训练过程中拒绝方向（r-direction）发生漂移，这是安全风险的主要原因。

**核心思路**：论文的核心思路是通过约束训练过程中隐藏状态在拒绝方向上的投影，来稳定r-direction，从而减轻安全风险。这种方法基于对LLM内部机制的理解，并试图通过正则化训练过程来保持模型的安全性。

**技术框架**：ProCon方法主要包含以下几个阶段：1) 确定拒绝方向（r-direction）；2) 在训练过程中，计算每个训练样本的隐藏状态在r-direction上的投影；3) 引入一个投影约束损失项，该损失项正则化投影的幅度，防止r-direction漂移；4) 采用warm-up策略，在训练初期施加更强的约束，并扩大数据分布以增强约束信号。

**关键创新**：最重要的技术创新点在于引入了投影约束损失项，并结合warm-up策略，直接干预训练过程中的r-direction漂移。与现有方法相比，ProCon方法更注重对LLM内部机制的理解和利用，通过约束关键的内部表示来提高安全性。

**关键设计**：关键设计包括：1) 投影约束损失函数的设计，需要平衡安全性和性能；2) warm-up策略的参数设置，包括初始约束强度和衰减策略；3) 数据增强策略，扩大数据分布以增强约束信号。具体而言，损失函数可以设计为投影幅度与目标值之间的距离，warm-up策略可以采用线性或指数衰减，数据增强可以采用对抗样本生成等方法。

## 📊 实验亮点

实验结果表明，ProCon方法在各种数据集、场景和LLM下，能够显著降低IFT带来的安全风险，同时保持任务性能的提升。与现有基线方法相比，ProCon方法在安全性和性能方面都取得了更好的平衡，尤其是在稳定r-direction方面表现出色。

## 🎯 应用场景

该研究成果可应用于各种需要安全保障的大语言模型应用场景，例如智能客服、内容生成、代码生成等。通过稳定模型的拒绝恶意指令能力，可以有效防止模型被用于恶意目的，提高用户信任度，并为未来安全AI研究奠定基础。

## 📄 摘要（原文）

> Instruction Fine-Tuning (IFT) has been widely adopted as an effective post-training strategy to enhance various abilities of Large Language Models (LLMs). However, prior studies have shown that IFT can significantly compromise LLMs' safety, particularly their ability to refuse malicious instructions, raising significant concerns. Recent research into the internal mechanisms of LLMs has identified the refusal direction (r-direction) in the hidden states, which plays a pivotal role in governing refusal behavior. Building on this insight, our study reveals that the r-direction tends to drift during training, which we identify as one of the causes of the associated safety risks. To mitigate such drift, our proposed ProCon method introduces a projection-constrained loss term that regularizes the projection magnitude of each training sample's hidden state onto the r-direction. Our initial analysis shows that applying an appropriate constraint can effectively mitigate the refusal direction drift and associated safety risks, but remains limited by overall performance barriers. To overcome this barrier, informed by our observation of early-stage sharp drift and a data-driven perspective, we introduce a warm-up strategy that emphasizes early-stage strong constraints and broaden the data distribution to strengthen constraint signals, leading to an enhanced ProCon method. Experimental results under various datasets, scenarios, and LLMs demonstrate that our method can significantly mitigate safety risks posed by IFT while preserving task performance gains. Even compared with strong baselines, our method consistently delivers superior overall performance. Crucially, our analysis indicates that ProCon can contribute to stabilizing the r-direction during training, while such an interpretability-driven exploration of LLMs' internal mechanisms lays a solid foundation for future safety research.

