---
layout: default
title: "DISCO: Disentangled Communication Steering for Large Language Models"
---

# DISCO: Disentangled Communication Steering for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16820" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16820v1</a>
  <a href="https://arxiv.org/pdf/2509.16820.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16820v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16820v1', 'DISCO: Disentangled Communication Steering for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Max Torop, Aria Masoomi, Masih Eskandar, Jennifer Dy

**分类**: cs.LG

**发布日期**: 2025-09-20

---

## 💡 一句话要点

**DISCO：通过解耦通信引导大型语言模型，提升控制粒度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `steering vector` `注意力机制` `解耦通信` `模型引导`

## 📋 核心要点

1. 现有steering vector方法在residual stream或attention head输出上添加向量，控制粒度受限。
2. DISCO直接在attention head的query和value空间注入steering vector，实现更精细的控制。
3. 实验表明，DISCO在多个数据集上优于现有方法，steering efficacy提升高达19.1%。

## 📝 摘要（中文）

本文提出了一种名为解耦通信（DISCO）引导的新方法，用于在推理时引导大型语言模型的输出。与以往将引导向量添加到残差流或注意力头表示的方法不同，DISCO直接将引导向量注入到注意力头内的查询和值表示空间中。研究表明，这些空间比注意力头输出更能线性区分概念，这正是使用引导向量的关键动机。论文分析了DISCO对注意力头输出的影响，揭示了DISCO解耦了一种强大的基线方法，即引导注意力输入，该方法以刚性方式隐式地修改查询和值。相比之下，DISCO直接调制这些组件，从而实现更精细的控制。在LLaMA 3.1 8B和Gemma 2 9B的多个数据集上，DISCO优于多个引导向量基线，引导效果评分比第二名高出高达19.1%。结果表明，查询和值空间是引导向量方法的强大构建块。

## 🔬 方法详解

**问题定义**：现有的大型语言模型引导方法，例如通过在残差流或注意力头输出中添加steering vector，存在控制粒度不足的问题。这些方法通常以较为僵化的方式影响模型的行为，难以实现精细化的干预和引导。因此，需要一种更灵活、更有效的引导方法，以更好地控制大型语言模型的输出。

**核心思路**：DISCO的核心思路是将steering vector直接注入到注意力头内的查询（query）和值（value）表示空间中。作者认为，相比于注意力头的输出，查询和值空间更能线性区分概念，因此更适合作为steering vector的作用对象。通过直接调制查询和值，DISCO能够更精细地控制注意力机制的行为，从而实现更有效的模型引导。

**技术框架**：DISCO方法主要包含以下几个步骤：1）选择需要引导的注意力头；2）获取该注意力头的查询和值表示；3）将steering vector注入到查询和值表示空间中；4）通过修改后的查询和值计算注意力权重和输出；5）将修改后的输出传递到后续层。整个过程在推理时进行，无需重新训练模型。

**关键创新**：DISCO最重要的技术创新点在于将steering vector的作用对象从注意力头输出转移到查询和值表示空间。这种改变使得引导过程更加灵活，能够实现更精细的控制。与以往隐式地修改查询和值的方法相比，DISCO直接调制这些组件，从而避免了信息损失和不必要的约束。

**关键设计**：DISCO的关键设计包括：1）steering vector的获取方式，可以通过训练或人工设计得到；2）steering vector的注入方式，例如直接相加或通过线性变换；3）注入steering vector的比例，需要根据具体任务进行调整；4）选择哪些注意力头进行引导，可以通过重要性分析或经验选择。

## 📊 实验亮点

实验结果表明，DISCO在LLaMA 3.1 8B和Gemma 2 9B等大型语言模型上取得了显著的性能提升。在多个数据集上，DISCO的steering efficacy评分比第二名高出高达19.1%。这些结果表明，查询和值空间是引导向量方法的强大构建块，DISCO能够有效地利用这些空间来实现更精细的模型控制。

## 🎯 应用场景

DISCO具有广泛的应用前景，例如可以用于控制大型语言模型的生成风格、提高模型的安全性、增强模型的可解释性等。在对话系统中，DISCO可以用于引导模型生成更符合用户意图的回复。在内容生成领域，DISCO可以用于控制模型生成特定主题或风格的文章。此外，DISCO还可以用于调试和优化大型语言模型，提高模型的性能和鲁棒性。

## 📄 摘要（原文）

> A variety of recent methods guide large language model outputs via the inference-time addition of steering vectors to residual-stream or attention-head representations. In contrast, we propose to inject steering vectors directly into the query and value representation spaces within attention heads. We provide evidence that a greater portion of these spaces exhibit high linear discriminability of concepts --a key property motivating the use of steering vectors-- than attention head outputs. We analytically characterize the effect of our method, which we term DISentangled COmmunication (DISCO) Steering, on attention head outputs. Our analysis reveals that DISCO disentangles a strong but underutilized baseline, steering attention inputs, which implicitly modifies queries and values in a rigid manner. In contrast, DISCO's direct modulation of these components enables more granular control. We find that DISCO achieves superior performance over a number of steering vector baselines across multiple datasets on LLaMA 3.1 8B and Gemma 2 9B, with steering efficacy scoring up to 19.1% higher than the runner-up. Our results support the conclusion that the query and value spaces are powerful building blocks for steering vector methods.

