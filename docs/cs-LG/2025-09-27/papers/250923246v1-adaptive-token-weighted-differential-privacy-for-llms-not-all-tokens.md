---
layout: default
title: "Adaptive Token-Weighted Differential Privacy for LLMs: Not All Tokens Require Equal Protection"
---

# Adaptive Token-Weighted Differential Privacy for LLMs: Not All Tokens Require Equal Protection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23246" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23246v1</a>
  <a href="https://arxiv.org/pdf/2509.23246.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23246v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23246v1', 'Adaptive Token-Weighted Differential Privacy for LLMs: Not All Tokens Require Equal Protection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Manjiang Yu, Priyanka Singh, Xue Li, Yang Cao

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-27

**备注**: 18 pages

---

## 💡 一句话要点

**提出自适应Token加权差分隐私(ATDP)方法，加速LLM的差分隐私训练并提升敏感信息保护。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `差分隐私` `大型语言模型` `隐私保护` `自适应加权` `敏感信息`

## 📋 核心要点

1. 现有DPSGD方法对所有梯度注入统一噪声，导致LLM训练时间过长且精度下降。
2. ATDP通过自适应地调整敏感和非敏感token的梯度权重，集中噪声于敏感token，从而加速训练。
3. 实验表明，ATDP能显著减少DP训练时间（约90%），同时保持或提升隐私保护和模型精度。

## 📝 摘要（中文）

大型语言模型(LLM)经常会记忆敏感或个人信息，引发了严重的隐私问题。现有的差分隐私随机梯度下降(DPSGD)变体对每个梯度步骤注入统一噪声，显著延长了训练时间并降低了模型精度。本文提出，将噪声主要集中在与敏感token相关的梯度上，可以显著减少DP训练时间，加强对敏感信息的保护，同时保持模型在非敏感数据上的性能。为此，本文提出自适应Token加权差分隐私(ATDP)，它是vanilla DP-SGD的改进版本，自适应地为敏感和非敏感token分配不同的梯度权重。通过在训练早期阶段采用更大的噪声尺度，ATDP迅速扰乱了对敏感内容的记忆。因此，ATDP仅需要在标准微调后进行几个额外的轻量级后处理epoch，主要针对与敏感token对应的参数注入有针对性的噪声，从而最大限度地减少对模型通用能力的影响。ATDP可以无缝集成到任何现有的基于DP的微调pipeline中，或者直接应用于非私有模型，作为一种快速的隐私增强措施。此外，结合初始的redacted微调阶段，ATDP形成了一个简化的DP pipeline，实现了与最先进的DP-SGD方法相当的canary保护，显著降低了DP微调的计算开销，将训练时间缩短了约90%，同时实现了相当或更优越的隐私保护和最小的精度下降。

## 🔬 方法详解

**问题定义**：大型语言模型容易记忆训练数据中的敏感信息，直接发布存在隐私泄露风险。传统的差分隐私训练方法，如DPSGD，通过在梯度中添加噪声来保护隐私，但这种方法会显著增加训练时间和降低模型性能。现有的方法无法在隐私保护、模型性能和训练效率之间取得良好的平衡。

**核心思路**：论文的核心思路是并非所有token都需要同等程度的隐私保护。敏感token（例如，包含个人信息的token）比非敏感token更需要保护。因此，可以自适应地调整不同token的梯度权重，对敏感token的梯度施加更大的噪声，从而在保证隐私的同时，减少对模型整体性能的影响，并加速训练过程。

**技术框架**：ATDP方法主要包含以下几个阶段：1) 标准模型微调：首先使用标准方法对模型进行微调，使其具备基本的语言能力。2) 敏感信息擦除（可选）：使用redacted fine-tuning方法，初步减少模型对敏感信息的记忆。3) 自适应Token加权：根据token的敏感程度，自适应地调整梯度权重。敏感token的梯度权重较高，非敏感token的梯度权重较低。4) 差分隐私训练：使用调整后的梯度权重进行DPSGD训练，对梯度添加噪声以保护隐私。5) 轻量级后处理：在DP训练后，进行少量的额外训练，以进一步提升模型性能。

**关键创新**：ATDP的关键创新在于自适应的token加权机制。它能够根据token的敏感程度动态地调整梯度权重，从而实现更精细化的隐私保护。与传统的DPSGD方法相比，ATDP能够更有效地利用噪声预算，在保证隐私的同时，减少对模型性能的影响。此外，ATDP可以与现有的DP训练pipeline无缝集成，具有良好的通用性。

**关键设计**：ATDP的关键设计包括：1) Token敏感度评估：需要一种方法来评估token的敏感程度。论文中可能使用了启发式方法或预训练的敏感度检测模型。2) 梯度权重调整策略：需要设计一种策略，根据token的敏感程度来调整梯度权重。例如，可以使用一个函数将token的敏感度映射到梯度权重。3) 噪声尺度调整：在训练的不同阶段，可以调整噪声的尺度。例如，在训练初期可以使用较大的噪声尺度，以快速扰乱模型对敏感信息的记忆。4) 损失函数：可以使用标准的交叉熵损失函数，或者根据具体任务进行调整。

## 📊 实验亮点

ATDP在实验中表现出显著的优势。与传统的DPSGD方法相比，ATDP能够将DP训练时间缩短约90%，同时实现相当或更优越的隐私保护和最小的精度下降。在canary保护方面，ATDP达到了与最先进的DP-SGD方法相当的水平。这些结果表明，ATDP是一种高效且有效的LLM隐私保护方法。

## 🎯 应用场景

ATDP可应用于各种需要保护用户隐私的LLM应用场景，例如：医疗健康领域的病历分析、金融领域的交易记录分析、教育领域的个性化辅导等。该方法能够有效防止LLM泄露用户敏感信息，同时保持模型的可用性，具有重要的实际应用价值和广阔的应用前景。

## 📄 摘要（原文）

> Large language models (LLMs) frequently memorize sensitive or personal information, raising significant privacy concerns. Existing variants of differential privacy stochastic gradient descent (DPSGD) inject uniform noise into every gradient step, significantly extending training time and reducing model accuracy. We propose that concentrating noise primarily on gradients associated with sensitive tokens can substantially decrease DP training time, strengthen the protection of sensitive information, and simultaneously preserve the model's performance on non-sensitive data. We operationalize this insight through Adaptive Token-Weighted Differential Privacy (ATDP), a modification of vanilla DP-SGD that adaptively assigns different gradient weights to sensitive and non-sensitive tokens. By employing a larger noise scale at the early stage of training, ATDP rapidly disrupts memorization of sensitive content. As a result, ATDP only requires a few additional epochs of lightweight post-processing following standard fine-tuning, injecting targeted noise primarily on parameters corresponding to sensitive tokens, thus minimally affecting the model's general capabilities. ATDP can be seamlessly integrated into any existing DP-based fine-tuning pipeline or directly applied to non-private models as a fast privacy-enhancing measure. Additionally, combined with an initial redacted fine-tuning phase, ATDP forms a streamlined DP pipeline that achieves comparable canary protection to state-of-the-art DP-SGD methods, significantly reduces the computational overhead of DP fine-tuning, shortening training time by approximately 90 percent, while achieving comparable or superior privacy protection and minimal accuracy degradation.

