---
layout: default
title: "DSDE: Dynamic Speculative Decoding with KLD Stability for Real-World Serving"
---

# DSDE: Dynamic Speculative Decoding with KLD Stability for Real-World Serving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01083" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01083v3</a>
  <a href="https://arxiv.org/pdf/2509.01083.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01083v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01083v3', 'DSDE: Dynamic Speculative Decoding with KLD Stability for Real-World Serving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingyu Yang, Jae-Young Choi, Kihyo Moon, Minsung Jang, Eunjoo Jeon

**分类**: cs.DC, cs.AI, cs.IT

**发布日期**: 2025-09-01 (更新: 2025-10-30)

**备注**: Accepted for presentation at the IEEE BigData 2025 Workshop (Special Session on Intelligent Data Mining). This v2 updates formatting and adds IEEE copyright notice

---

## 💡 一句话要点

**提出动态推测解码引擎DSDE以解决大批量服务中的推测长度问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `动态推测解码` `KLD散度` `大语言模型` `解码效率` `鲁棒性` `自适应推测长度` `实时推理` `多样化请求`

## 📋 核心要点

1. 现有的推测解码方法依赖固定的推测长度，无法有效应对多样化请求带来的挑战。
2. 本文提出的DSDE框架通过KLD散度的方差信号实现动态推测长度的自适应调整，提升了解码效率。
3. 实验结果显示，DSDE在端到端延迟上与现有方法相当，并在低接受率场景中表现出更好的鲁棒性。

## 📝 摘要（中文）

推测解码加速了大型语言模型的推理，但在多样化请求的大批量服务环境中，固定的推测长度并不理想。本文探索了一种动态适应的新方向，提出了动态推测解码引擎（DSDE），该框架基于两大核心组件：一种基于Kullback-Leibler（KLD）散度方差的预测信号，用于诊断生成的区域稳定性，以及一个自适应的推测长度上限，以缓解每个序列解码中的滞后问题。实验表明，基于KLD的稳定性信号在动态适应中的潜力，所提出的算法在端到端延迟上与领先基线竞争，并在多样化工作负载中展现出更强的鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有推测解码方法在大批量服务环境中固定推测长度带来的效率低下问题。现有方法无法适应多样化请求，导致解码延迟和资源浪费。

**核心思路**：DSDE框架通过引入基于KLD散度方差的预测信号，实现动态推测长度的自适应调整，从而提高解码的灵活性和效率。该设计旨在根据生成过程的稳定性动态调整推测长度，以应对不同请求的需求。

**技术框架**：DSDE框架主要由两个组件构成：首先是KLD散度方差预测信号，用于评估生成过程的区域稳定性；其次是自适应推测长度上限，旨在解决每个序列解码中的滞后问题。整体流程包括信号生成、推测长度调整和解码执行三个阶段。

**关键创新**：最重要的技术创新在于利用KLD散度的方差作为动态适应信号，这一方法与传统的固定推测长度策略本质上不同，能够根据实时反馈调整解码策略。

**关键设计**：在设计中，KLD散度的计算方法和阈值设置是关键，确保信号的准确性和实时性。此外，推测长度的自适应上限设计也考虑了不同请求的特性，以优化解码过程。

## 📊 实验亮点

实验结果表明，DSDE在端到端延迟上与领先基线相当，且在低接受率的情况下，鲁棒性显著增强。具体而言，基于KLD的动态适应信号在多样化工作负载下展现出优越的性能，验证了其在实际应用中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括大型语言模型的实时推理服务、智能客服系统和多模态交互平台等。通过提高解码效率和鲁棒性，DSDE能够在实际应用中显著提升用户体验，降低延迟，适应多样化的请求场景，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Speculative decoding accelerates large language model inference, but its reliance on a fixed speculation length is suboptimal in large-batch serving environments with diverse requests. This paper explores a new direction for dynamic adaptation by investigating a novel class of post-hoc, diagnostic signals. We propose Dynamic Speculative Decoding Engine (DSDE), a training-free framework built on two primary components: (1) a predictive signal based on the variance of the Kullback-Leibler (KLD) divergence, which diagnoses the generation's regional stability, and (2) an adaptive speculation length cap to mitigate the straggler problem in per-sequence decoding. Experiments demonstrate the potential of using KLD-based stability signals for dynamic adaptation. An algorithm guided by these signals achieves end-to-end latency competitive with leading baselines and exhibits superior robustness across diverse workloads. This robustness is particularly valuable in challenging low-acceptance-rate regimes, where the proposed signal maintains its diagnostic utility. Collectively, these findings validate post-hoc signals as a valuable component for building more robust and intelligent LLM inference systems, and highlight a promising direction for future research on dynamic speculation length adaptation.

