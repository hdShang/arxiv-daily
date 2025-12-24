---
layout: default
title: "ENSI: Efficient Non-Interactive Secure Inference for Large Language Models"
---

# ENSI: Efficient Non-Interactive Secure Inference for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09424" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09424v1</a>
  <a href="https://arxiv.org/pdf/2509.09424.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09424v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09424v1', 'ENSI: Efficient Non-Interactive Secure Inference for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiyu He, Maojiang Wang, Xinwen Gao, Yuchuan Luo, Lin Liu, Shaojing Fu

**分类**: cs.CR, cs.AI

**发布日期**: 2025-09-11

---

## 💡 一句话要点

**ENSI：面向大语言模型的高效非交互安全推理框架**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `安全推理` `同态加密` `大语言模型` `BitNet` `隐私保护`

## 📋 核心要点

1. 现有安全推理方法在处理大语言模型时，由于密码协议的复杂性以及LLM的巨大参数规模和复杂架构，实用性受到严重限制。
2. ENSI框架通过协同设计密码协议和LLM架构，优化编码策略，并采用BitNet等轻量级模型，降低加密计算的复杂度。
3. 实验结果表明，ENSI在矩阵乘法和softmax推理速度上均优于现有方法，并显著降低了自举操作的比例。

## 📝 摘要（中文）

本文提出ENSI，一种新颖的非交互式大语言模型安全推理框架，其核心在于密码协议与LLM架构的协同设计。ENSI采用优化的编码策略，将CKKS方案与轻量级LLM变体BitNet无缝集成，显著降低了加密矩阵乘法的计算复杂度。针对同态加密（HE）下softmax计算量过大的问题，首创性地将sigmoid注意力机制与HE集成，作为一种无缝且无需重新训练的替代方案。此外，通过将自举操作嵌入到RMSNorm过程中，高效地刷新密文，同时显著降低了代价高昂的自举调用的频率。实验评估表明，与最先进的方法相比，ENSI在CPU上实现了约8倍的矩阵乘法加速和2.6倍的softmax推理加速，自举比例降低到仅1%。

## 🔬 方法详解

**问题定义**：现有安全推理方法在应用于大语言模型时面临巨大的计算挑战。传统的同态加密方案与LLM的结合，由于LLM参数量巨大以及复杂的计算模式，导致计算开销过高，难以实际应用。特别是softmax操作，在同态加密下计算复杂度极高，成为性能瓶颈。

**核心思路**：ENSI的核心思路是通过密码协议与LLM架构的协同设计，降低加密计算的复杂度。具体来说，通过选择计算复杂度较低的LLM变体（BitNet），并优化编码方式，使得同态加密后的计算更加高效。同时，采用sigmoid注意力机制替代softmax，避免了高昂的同态加密softmax计算。此外，通过将自举操作融入RMSNorm，减少了自举的频率。

**技术框架**：ENSI框架主要包含以下几个关键模块：1) 优化的CKKS编码策略，用于高效地将数据编码为密文；2) 基于BitNet的轻量级LLM架构，降低了计算复杂度；3) 基于sigmoid的注意力机制，替代了softmax，避免了复杂的同态加密计算；4) 集成自举操作的RMSNorm层，用于刷新密文并减少自举频率。整体流程为：首先使用优化的编码策略将输入数据加密，然后通过BitNet进行推理，其中使用sigmoid注意力机制替代softmax，并在RMSNorm层进行自举操作，最后输出加密的推理结果。

**关键创新**：ENSI的关键创新在于密码协议与LLM架构的协同设计。具体体现在以下几个方面：1) 针对同态加密的特性，选择了计算复杂度较低的BitNet作为LLM的基础架构；2) 提出了优化的CKKS编码策略，降低了加密计算的开销；3) 首创性地将sigmoid注意力机制与同态加密结合，替代了softmax，解决了同态加密下softmax计算复杂度过高的问题；4) 将自举操作嵌入到RMSNorm层中，减少了自举的频率，提高了整体性能。

**关键设计**：ENSI的关键设计包括：1) CKKS编码策略的优化，具体编码方式未知；2) BitNet的具体配置参数未知；3) Sigmoid注意力机制的实现细节，包括具体的公式和参数设置未知；4) RMSNorm层中自举操作的嵌入方式，包括自举的具体算法和参数设置未知。

## 📊 实验亮点

ENSI在实验中表现出显著的性能提升。与现有最先进的方法相比，ENSI在CPU上实现了约8倍的矩阵乘法加速和2.6倍的softmax推理加速。更重要的是，自举操作的比例降低到仅1%，这表明ENSI能够显著降低同态加密的计算开销，使其更适用于实际应用。

## 🎯 应用场景

ENSI在保护用户隐私的大语言模型应用中具有广泛的应用前景，例如：隐私保护的智能客服、安全医疗诊断、金融风控等。该研究成果有助于推动安全人工智能的发展，使得在保护用户敏感数据的前提下，也能充分利用大语言模型的强大能力。未来，ENSI有望应用于更多需要隐私保护的场景，并促进相关技术的进一步发展。

## 📄 摘要（原文）

> Secure inference enables privacy-preserving machine learning by leveraging cryptographic protocols that support computations on sensitive user data without exposing it. However, integrating cryptographic protocols with large language models (LLMs) presents significant challenges, as the inherent complexity of these protocols, together with LLMs' massive parameter scale and sophisticated architectures, severely limits practical usability. In this work, we propose ENSI, a novel non-interactive secure inference framework for LLMs, based on the principle of co-designing the cryptographic protocols and LLM architecture. ENSI employs an optimized encoding strategy that seamlessly integrates CKKS scheme with a lightweight LLM variant, BitNet, significantly reducing the computational complexity of encrypted matrix multiplications. In response to the prohibitive computational demands of softmax under homomorphic encryption (HE), we pioneer the integration of the sigmoid attention mechanism with HE as a seamless, retraining-free alternative. Furthermore, by embedding the Bootstrapping operation within the RMSNorm process, we efficiently refresh ciphertexts while markedly decreasing the frequency of costly bootstrapping invocations. Experimental evaluations demonstrate that ENSI achieves approximately an 8x acceleration in matrix multiplications and a 2.6x speedup in softmax inference on CPU compared to state-of-the-art method, with the proportion of bootstrapping is reduced to just 1%.

