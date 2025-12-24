---
layout: default
title: "MoGU V2: Toward a Higher Pareto Frontier Between Model Usability and Security"
---

# MoGU V2: Toward a Higher Pareto Frontier Between Model Usability and Security

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.06807" class="toolbar-btn" target="_blank">📄 arXiv: 2509.06807v1</a>
  <a href="https://arxiv.org/pdf/2509.06807.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.06807v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.06807v1', 'MoGU V2: Toward a Higher Pareto Frontier Between Model Usability and Security')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanrui Du, Fenglei Fan, Sendong Zhao, Jiawei Cao, Ting Liu, Bing Qin

**分类**: cs.CL

**发布日期**: 2025-09-08

---

## 💡 一句话要点

**MoGU V2：提升LLM可用性与安全性帕累托前沿，解决安全与可用性trade-off问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型安全` `可用性优化` `动态路由` `指令微调` `安全风险缓解`

## 📋 核心要点

1. 现有LLM安全方法常以牺牲可用性为代价，导致保守的拒绝式响应，无法兼顾安全与实用。
2. MoGU V2通过更紧密的路由器与隐藏状态耦合，动态调整安全和可用性优化模块的权重，实现双向适应。
3. MoGU V2在主流、设备端和推理LLM上均表现出强大的适应性和安全性提升，且易于恢复指令微调带来的安全风险。

## 📝 摘要（中文）

随着大型语言模型（LLMs）日益普及，其安全性已成为关键问题，特别是对恶意指令保持无害响应的能力。虽然现有方法在提高LLMs安全性方面取得进展，但往往导致保守、拒绝式的响应，从而损害了实际可用性。这带来了一个关键挑战：如何在LLMs的可用性和安全性之间提升帕累托前沿，而不是进行权衡。为此，我们提出了MoGU框架，其中层内路由器通过感知隐藏状态动态分配权重，从而平衡安全优化和可用性优化变体的贡献。MoGU框架面临参数冗余和性能瓶颈等限制。为了克服这些问题，我们进一步提出了改进的MoGU_v2框架，该框架在路由器和隐藏状态之间建立了更紧密的耦合。在MoGU_v2中，路由器仅嵌入在编码高度可分类安全特征的层中，并且在路由器优化期间激活骨干模块以实现双向适应。MoGU_V2在各种LLMs系列中表现出强大的适应性和稳定的改进，包括主流LLMs、设备端LLMs和推理LLMs。同时，即使面对指令微调带来的风险，MoGU_v2也可以通过简单的数据混合策略轻松恢复安全性，而不会影响任务性能的提升。这些全面的改进突显了MoGU_V2作为缓解实际应用中安全风险的强大而通用的解决方案。

## 🔬 方法详解

**问题定义**：大型语言模型（LLMs）的安全性日益重要，尤其是在面对恶意指令时。然而，现有的安全方法往往过于保守，导致模型拒绝回答许多问题，严重影响了LLMs的可用性。因此，如何在保证安全性的同时，最大限度地提高LLMs的可用性，成为了一个亟待解决的问题。现有方法的痛点在于安全性和可用性之间存在trade-off，难以兼顾。

**核心思路**：MoGU V2的核心思路是通过动态地调整模型中不同模块的权重，从而在安全性和可用性之间找到一个更好的平衡点。具体来说，MoGU V2引入了路由器（router）机制，根据模型的隐藏状态来动态地分配权重给安全优化模块和可用性优化模块。这种动态调整使得模型能够根据不同的输入，灵活地选择合适的模块进行处理，从而在保证安全性的同时，提高可用性。

**技术框架**：MoGU V2的整体架构包括以下几个主要模块：1）骨干网络（backbone）：负责处理输入并生成隐藏状态；2）路由器（router）：根据隐藏状态动态地分配权重给不同的模块；3）安全优化模块：负责提高模型的安全性，例如过滤恶意指令；4）可用性优化模块：负责提高模型的可用性，例如生成更自然、更流畅的回答。在训练过程中，路由器会根据模型的表现进行优化，从而学习到如何在不同的情况下选择合适的模块。

**关键创新**：MoGU V2最重要的技术创新点在于路由器与隐藏状态的紧密耦合。与之前的MoGU框架相比，MoGU V2只在编码高度可分类安全特征的层中嵌入路由器，并且在路由器优化期间激活骨干模块，从而实现双向适应。这种设计使得路由器能够更好地理解模型的内部状态，并根据不同的情况做出更明智的决策。此外，MoGU V2还采用了一种简单的数据混合策略，可以轻松恢复指令微调带来的安全风险，而不会影响任务性能的提升。

**关键设计**：MoGU V2的关键设计包括：1）路由器的位置：只在编码高度可分类安全特征的层中嵌入路由器，以减少参数冗余和提高效率；2）骨干模块的激活：在路由器优化期间激活骨干模块，以实现双向适应；3）数据混合策略：采用一种简单的数据混合策略，可以轻松恢复指令微调带来的安全风险。

## 📊 实验亮点

MoGU V2在各种LLM系列中表现出强大的适应性和稳定的改进，包括主流LLMs、设备端LLMs和推理LLMs。实验结果表明，MoGU V2可以在保证安全性的前提下，显著提高LLMs的可用性。即使面对指令微调带来的风险，MoGU V2也可以通过简单的数据混合策略轻松恢复安全性，而不会影响任务性能的提升。这些结果表明，MoGU V2是一种有效且通用的LLM安全解决方案。

## 🎯 应用场景

MoGU V2具有广泛的应用前景，可以应用于各种需要保证安全性的LLM应用场景，例如智能客服、聊天机器人、内容生成等。尤其是在金融、医疗等对安全性要求较高的领域，MoGU V2可以有效地降低LLM被恶意利用的风险，保障用户的信息安全。此外，MoGU V2还可以应用于设备端LLM，在资源受限的情况下，实现安全性和可用性的平衡。

## 📄 摘要（原文）

> As Large Language Models (LLMs) increasingly permeate human life, their security has emerged as a critical concern, particularly their ability to maintain harmless responses to malicious instructions. Although extensive methods have improved LLMs' security, they often lead to conservative, rejection-oriented responses that compromise practical usability. This presents a key challenge: how to advance the Pareto frontier between LLMs' usability and security, rather than necessitate a trade-off between them. To address this, we propose the MoGU framework, in which the intra-layer router dynamically allocates weights by sensing hidden states, thereby balancing the contributions of security-optimized and usability-optimized variants. Despite its initial potential, the MoGU framework faces limitations such as parameter redundancy and performance bottlenecks. To overcome these, we further propose an improved MoGU_v2 framework that establishes a tighter coupling between the routers and hidden states. In MoGU_v2, routers are embedded only in layers encoding highly classifiable security features, and backbone modules are activated during router optimization to enable bidirectional adaptation. MoGU_V2 exhibits strong adaptability and stable improvements across various series of LLMs, including mainstream LLMs serving as brains in various applications, on-device LLMs optimized for resource-constrained scenarios, and reasoning LLMs tailored for user interpretability. Meanwhile, even facing risks introduced by Instruction Fine-tuning, MoGU_v2 can easily restore security without compromising the task performance gains via a simple data-mix strategy. These comprehensive improvements highlight MoGU_V2 as a robust and versatile solution for mitigating security risks in real-world applications.

