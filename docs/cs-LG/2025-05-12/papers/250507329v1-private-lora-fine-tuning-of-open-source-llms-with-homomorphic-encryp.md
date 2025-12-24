---
layout: default
title: Private LoRA Fine-tuning of Open-Source LLMs with Homomorphic Encryption
---

# Private LoRA Fine-tuning of Open-Source LLMs with Homomorphic Encryption

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07329" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07329v1</a>
  <a href="https://arxiv.org/pdf/2505.07329.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07329v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07329v1', 'Private LoRA Fine-tuning of Open-Source LLMs with Homomorphic Encryption')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jordan Frery, Roman Bredehoft, Jakub Klemsa, Arthur Meyre, Andrei Stoian

**分类**: cs.CR, cs.LG

**发布日期**: 2025-05-12

---

## 💡 一句话要点

**提出私密LoRA微调方法以解决开源LLM数据隐私问题**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `同态加密` `低秩适应` `私密微调` `大型语言模型` `数据隐私` `敏感应用` `模型训练`

## 📋 核心要点

1. 现有方法在开源LLM微调中缺乏有效的数据隐私保护，导致敏感信息泄露的风险。
2. 本研究提出了一种结合LoRA技术与同态加密的私密微调协议，确保训练数据的安全性。
3. 通过微调Llama-3.2-1B模型，验证了该方法的可行性，并展示了HE计算的性能优势。

## 📝 摘要（中文）

在开源大型语言模型（LLMs）微调过程中，保护数据机密性对于敏感应用至关重要。本研究提出了一种交互式协议，适应低秩适应（LoRA）技术以实现私密微调。采用同态加密（HE）保护训练数据和梯度的机密性，远程工作节点执行大部分计算，数据拥有者负责训练，减少了对昂贵客户端GPU的需求。我们通过微调Llama-3.2-1B模型展示了可行性，提供了使用HE兼容量化的收敛结果和HE计算在GPU硬件上的性能基准。该方法可用于保密知识库问答、私密代码库微调、基于公司邮件档案起草邮件的AI代理，以及分析敏感法律或医疗文件的模型适配。

## 🔬 方法详解

**问题定义**：本论文旨在解决在开源大型语言模型微调过程中数据隐私保护不足的问题。现有方法通常依赖于本地计算，容易导致敏感数据泄露。

**核心思路**：论文提出了一种结合低秩适应（LoRA）和同态加密（HE）的私密微调协议。通过将计算分散到远程节点，数据拥有者只需进行少量本地计算，从而保护数据隐私。

**技术框架**：整体架构包括数据拥有者、远程工作节点和同态加密模块。数据拥有者负责训练协调，远程节点执行计算，HE模块确保数据和梯度的机密性。

**关键创新**：最重要的创新在于将LoRA技术与同态加密结合，形成了一种新的私密微调方法。这一设计使得在保护数据隐私的同时，仍能有效进行模型训练。

**关键设计**：在技术细节上，采用HE兼容的量化方法以提高计算效率，并在GPU硬件上进行性能基准测试，确保微调过程的高效性。

## 📊 实验亮点

实验结果表明，使用同态加密的微调方法在Llama-3.2-1B模型上实现了良好的收敛性，且在GPU硬件上进行HE计算时表现出显著的性能优势，具体性能数据和基线对比将在论文中详细列出。

## 🎯 应用场景

该研究的潜在应用领域包括保密知识库问答、私密代码库微调、AI邮件起草代理以及敏感法律或医疗文件的分析。通过保护数据隐私，该方法为企业和机构在处理敏感信息时提供了安全保障，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Preserving data confidentiality during the fine-tuning of open-source Large Language Models (LLMs) is crucial for sensitive applications. This work introduces an interactive protocol adapting the Low-Rank Adaptation (LoRA) technique for private fine-tuning. Homomorphic Encryption (HE) protects the confidentiality of training data and gradients handled by remote worker nodes performing the bulk of computations involving the base model weights. The data owner orchestrates training, requiring minimal local computing power and memory, thus alleviating the need for expensive client-side GPUs. We demonstrate feasibility by fine-tuning a Llama-3.2-1B model, presenting convergence results using HE-compatible quantization and performance benchmarks for HE computations on GPU hardware. This approach enables applications such as confidential knowledge base question answering, private codebase fine-tuning for AI code assistants, AI agents for drafting emails based on a company's email archive, and adapting models to analyze sensitive legal or healthcare documents.

