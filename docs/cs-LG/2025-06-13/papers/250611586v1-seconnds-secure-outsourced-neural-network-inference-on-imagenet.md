---
layout: default
title: "SecONNds: Secure Outsourced Neural Network Inference on ImageNet"
---

# SecONNds: Secure Outsourced Neural Network Inference on ImageNet

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11586" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11586v1</a>
  <a href="https://arxiv.org/pdf/2506.11586.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11586v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11586v1', 'SecONNds: Secure Outsourced Neural Network Inference on ImageNet')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shashank Balla

**分类**: cs.CR, cs.LG

**发布日期**: 2025-06-13

**🔗 代码/项目**: [GITHUB](https://github.com/shashankballa/SecONNds)

---

## 💡 一句话要点

**提出SecONNds以解决安全外包神经网络推理隐私问题**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `安全推理` `神经网络` `隐私保护` `卷积神经网络` `GPU加速` `数论变换` `高效计算` `开源`

## 📋 核心要点

1. 现有的安全推理框架在计算开销和通信成本上存在显著不足，限制了其在实际应用中的可行性。
2. SecONNds通过集成新颖的GMW协议和NTT预处理，优化了大规模卷积神经网络的安全推理过程。
3. 在评估中，SecONNds在推理时间和通信量上表现出色，GPU推理时间为2.8秒，通信量仅为420 MiB。

## 📝 摘要（中文）

随着外包神经网络推理的广泛应用，用户数据在不可信的远程服务器上处理带来了显著的隐私挑战。尽管安全推理提供了保护隐私的解决方案，但现有框架存在高计算开销和通信成本的问题，使其在实际部署中不够可行。本文提出了SecONNds，一个针对大规模ImageNet卷积神经网络优化的非侵入式安全推理框架。SecONNds集成了一种新颖的完全布尔Goldreich-Micali-Wigderson（GMW）协议，用于安全比较，解决了Yao的百万富翁问题。我们的协议在非线性操作中实现了17倍的在线加速，同时减少了通信开销。通过使用数论变换（NTT）预处理和GPU加速，SecONNds在CPU和GPU上分别实现了线性操作的1.6倍和2.2倍加速。SecONNds-P是一个确保可验证全精度结果的位精确变体，能够与明文计算结果相匹配。经过评估，SecONNds在37位量化的SqueezeNet模型上实现了GPU端2.8秒和CPU端3.6秒的端到端推理时间，总通信量仅为420 MiB。SecONNds的高效性和降低的计算负载使其非常适合在资源受限环境中部署隐私敏感的应用。

## 🔬 方法详解

**问题定义**：本文旨在解决在不可信的远程服务器上进行神经网络推理时的隐私保护问题。现有方法在计算和通信开销上过高，导致实际应用受限。

**核心思路**：SecONNds通过引入GMW协议和NTT预处理，优化了安全推理的效率，旨在降低计算和通信成本，同时确保隐私保护。

**技术框架**：SecONNds的整体架构包括数据预处理、GMW协议的实现、NTT预处理模块以及GPU加速的同态加密操作。各模块协同工作以提高推理速度和安全性。

**关键创新**：最重要的创新在于提出了一种高效的GMW协议，解决了Yao的百万富翁问题，并在非线性操作中实现了17倍的加速，这在现有方法中是前所未有的。

**关键设计**：在设计中，使用了预处理的Beaver位三元组和Silent Random Oblivious Transfer，确保了协议的安全性和效率。此外，采用了数论变换（NTT）来优化线性操作的计算速度。

## 📊 实验亮点

SecONNds在评估中表现出色，GPU推理时间为2.8秒，CPU推理时间为3.6秒，通信量仅为420 MiB。与现有最先进的解决方案相比，SecONNds在非线性操作中实现了17倍的速度提升，同时在CPU和GPU上分别实现了1.6倍和2.2倍的加速，显示出其在安全推理中的优越性。

## 🎯 应用场景

SecONNds的研究成果具有广泛的应用潜力，特别是在需要保护用户隐私的领域，如医疗影像分析、金融数据处理和智能监控等。其高效的推理性能使其适合在资源受限的环境中部署，推动隐私保护技术的实际应用。未来，SecONNds可能会在更多的隐私敏感应用中得到推广和应用。

## 📄 摘要（原文）

> The widespread adoption of outsourced neural network inference presents significant privacy challenges, as sensitive user data is processed on untrusted remote servers. Secure inference offers a privacy-preserving solution, but existing frameworks suffer from high computational overhead and communication costs, rendering them impractical for real-world deployment. We introduce SecONNds, a non-intrusive secure inference framework optimized for large ImageNet-scale Convolutional Neural Networks. SecONNds integrates a novel fully Boolean Goldreich-Micali-Wigderson (GMW) protocol for secure comparison -- addressing Yao's millionaires' problem -- using preprocessed Beaver's bit triples generated from Silent Random Oblivious Transfer. Our novel protocol achieves an online speedup of 17$\times$ in nonlinear operations compared to state-of-the-art solutions while reducing communication overhead. To further enhance performance, SecONNds employs Number Theoretic Transform (NTT) preprocessing and leverages GPU acceleration for homomorphic encryption operations, resulting in speedups of 1.6$\times$ on CPU and 2.2$\times$ on GPU for linear operations. We also present SecONNds-P, a bit-exact variant that ensures verifiable full-precision results in secure computation, matching the results of plaintext computations. Evaluated on a 37-bit quantized SqueezeNet model, SecONNds achieves an end-to-end inference time of 2.8 s on GPU and 3.6 s on CPU, with a total communication of just 420 MiB. SecONNds' efficiency and reduced computational load make it well-suited for deploying privacy-sensitive applications in resource-constrained environments. SecONNds is open source and can be accessed from: https://github.com/shashankballa/SecONNds.

