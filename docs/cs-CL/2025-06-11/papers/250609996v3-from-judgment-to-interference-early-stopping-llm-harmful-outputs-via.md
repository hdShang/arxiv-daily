---
layout: default
title: "From Judgment to Interference: Early Stopping LLM Harmful Outputs via Streaming Content Monitoring"
---

# From Judgment to Interference: Early Stopping LLM Harmful Outputs via Streaming Content Monitoring

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09996" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09996v3</a>
  <a href="https://arxiv.org/pdf/2506.09996.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09996v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09996v3', 'From Judgment to Interference: Early Stopping LLM Harmful Outputs via Streaming Content Monitoring')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yang Li, Qiang Sheng, Yehan Yang, Xueyao Zhang, Juan Cao

**分类**: cs.CL, cs.CY

**发布日期**: 2025-06-11 (更新: 2025-09-22)

**备注**: NeurIPS 2025 Accepted Paper

---

## 💡 一句话要点

**提出流式内容监控以解决LLM有害输出的早期停止问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `内容监控` `有害输出` `实时检测` `安全对齐` `双重监督` `FineHarm数据集`

## 📋 核心要点

1. 现有的审核方法依赖完整输出的完全检测，导致服务延迟高且效率低下。
2. 本文提出流式内容监控器（SCM），通过双重监督实现对部分输出的实时监控与判断。
3. 实验结果显示，SCM在仅查看18%输出的情况下，宏F1分数达到0.95以上，性能与完全检测相当。

## 📝 摘要（中文）

尽管大多数大型语言模型（LLMs）已应用安全对齐，但LLM服务提供商通常在实际产品中部署后续的内容审核作为外部安全防护。现有的审核方法主要采用传统的完全检测，基于完整的LLM输出判断有害性，导致服务延迟较高。近期研究关注部分检测，即在生成过程中进行监控，若检测到有害性则提前停止输出，但直接将全检测训练的审核员应用于不完整输出，导致训练与推理之间存在差距，降低了性能。本文探讨如何形成一个原生支持部分检测的数据与模型解决方案，构建了FineHarm数据集，并提出了流式内容监控器（SCM），通过双重监督进行训练，能够及时判断有害性。实验表明，SCM在仅查看响应的前18%标记的情况下，宏F1分数超过0.95，性能与完全检测相当。

## 🔬 方法详解

**问题定义**：本文解决的问题是如何有效监控大型语言模型（LLM）输出中的有害内容，现有方法在完全检测中存在高延迟和性能下降的问题。

**核心思路**：论文的核心思路是通过构建流式内容监控器（SCM），实现对LLM输出的实时监控，采用双重监督机制来提高对部分输出的判断能力。

**技术框架**：整体架构包括FineHarm数据集的构建和SCM的设计。FineHarm数据集包含29K个带细粒度标注的提示-响应对，SCM则通过响应级和标记级标签进行训练，能够实时跟踪LLM的输出流。

**关键创新**：最重要的技术创新在于SCM的设计，它能够在输出生成的早期阶段进行有害性判断，避免了传统方法的训练-推理差距。

**关键设计**：SCM的训练采用双重监督，结合响应级和标记级标签，确保模型在部分输出的情况下也能有效判断有害性。

## 📊 实验亮点

实验结果显示，流式内容监控器（SCM）在仅查看响应的前18%标记的情况下，宏F1分数超过0.95，性能与传统的完全检测方法相当，且SCM能够作为伪有害性标注器，进一步提升安全对齐效果。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容审核、在线教育平台以及任何需要实时监控生成内容安全性的应用。通过提高对有害内容的检测能力，能够有效保护用户免受不当信息的影响，提升产品的安全性和用户体验。

## 📄 摘要（原文）

> Though safety alignment has been applied to most large language models (LLMs), LLM service providers generally deploy a subsequent moderation as the external safety guardrail in real-world products. Existing moderators mainly practice a conventional full detection, which determines the harmfulness based on the complete LLM output, causing high service latency. Recent works pay more attention to partial detection where moderators oversee the generation midway and early stop the output if harmfulness is detected, but they directly apply moderators trained with the full detection paradigm to incomplete outputs, introducing a training-inference gap that lowers the performance. In this paper, we explore how to form a data-and-model solution that natively supports partial detection. For the data, we construct FineHarm, a dataset consisting of 29K prompt-response pairs with fine-grained annotations to provide reasonable supervision for token-level training. Then, we propose the streaming content monitor, which is trained with dual supervision of response- and token-level labels and can follow the output stream of LLM to make a timely judgment of harmfulness. Experiments show that SCM gains 0.95+ in macro F1 score that is comparable to full detection, by only seeing the first 18% of tokens in responses on average. Moreover, the SCM can serve as a pseudo-harmfulness annotator for improving safety alignment and lead to a higher harmlessness score than DPO.

