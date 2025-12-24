---
layout: default
title: "Can AI Keep a Secret? Contextual Integrity Verification: A Provable Security Architecture for LLMs"
---

# Can AI Keep a Secret? Contextual Integrity Verification: A Provable Security Architecture for LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09288" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09288v2</a>
  <a href="https://arxiv.org/pdf/2508.09288.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09288v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09288v2', 'Can AI Keep a Secret? Contextual Integrity Verification: A Provable Security Architecture for LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aayush Gupta

**分类**: cs.CR, cs.AI, cs.CL

**发布日期**: 2025-08-12 (更新: 2025-08-18)

**备注**: 2 figures, 3 tables; code and certification harness: https://github.com/ayushgupta4897/Contextual-Integrity-Verification ; Elite-Attack dataset: https://huggingface.co/datasets/zyushg/elite-attack

---

## 💡 一句话要点

**提出上下文完整性验证以解决大语言模型安全问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `安全性` `上下文完整性` `提示注入` `加密签名` `信任格` `非干扰保证` `轻量级架构`

## 📋 核心要点

1. 现有的大语言模型在面对提示注入和越狱攻击时表现出明显的脆弱性，现有的防护措施常常无法有效阻止这些攻击。
2. 本文提出的上下文完整性验证（CIV）通过为每个标记附加加密签名的来源标签，确保低信任标记不会影响高信任表示，从而增强安全性。
3. 在基准测试中，CIV在指定的威胁模型下实现了0%的攻击成功率，同时保持了93.1%的标记级相似性，且未降低模型在良性任务上的表现。

## 📝 摘要（中文）

大语言模型（LLMs）在提示注入和相关越狱攻击方面仍然非常脆弱，现有的启发式防护措施（如规则、过滤器和LLM评估者）经常被绕过。本文提出了一种推理时安全架构——上下文完整性验证（CIV），该架构为每个标记附加了加密签名的来源标签，并通过预软最大化硬注意力掩码在变换器内部强制执行源信任格。CIV为冻结模型提供了确定性的每标记非干扰保证：低信任标记无法影响高信任表示。在基于最近提示注入向量分类法的基准测试中，CIV在所述威胁模型下实现了0%的攻击成功率，同时保持93.1%的标记级相似性，并且在良性任务上没有模型困惑度的下降；我们注意到由于未优化的数据路径导致的延迟开销。由于CIV是一个轻量级补丁——无需微调——我们展示了对Llama-3-8B和Mistral-7B的即插即用保护。我们发布了参考实现、自动认证工具和Elite-Attack语料库，以支持可重复研究。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在提示注入和越狱攻击中的安全脆弱性，现有方法无法有效防止这些攻击，导致模型输出不可靠或被操控。

**核心思路**：提出上下文完整性验证（CIV），通过为每个标记附加加密签名的来源标签，构建信任格，确保低信任标记不会影响高信任标记的表示，从而增强模型的安全性。

**技术框架**：CIV的整体架构包括为每个标记生成加密签名、构建信任格以及通过预软最大化硬注意力掩码来实施信任控制。该架构在推理阶段运行，确保模型的每个输出都受到保护。

**关键创新**：CIV的主要创新在于其提供的每标记非干扰保证，确保低信任标记不会影响高信任表示，这在现有的防护措施中是前所未有的。

**关键设计**：CIV采用了预软最大化硬注意力掩码，并结合可选的前馈网络/残差门控设计，以实现高效的信任控制。该方法无需对模型进行微调，具有轻量级的特点，便于快速部署。

## 📊 实验亮点

在实验中，CIV在指定的威胁模型下实现了0%的攻击成功率，显示出其卓越的安全性。同时，CIV保持了93.1%的标记级相似性，并未对模型在良性任务上的困惑度造成负面影响，证明了其有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括安全敏感的自然语言处理任务，如金融、医疗和法律等领域，能够有效防止模型被恶意操控，确保输出的可靠性和安全性。未来，CIV可能成为大语言模型安全防护的标准组件，推动更广泛的应用和信任建立。

## 📄 摘要（原文）

> Large language models (LLMs) remain acutely vulnerable to prompt injection and related jailbreak attacks; heuristic guardrails (rules, filters, LLM judges) are routinely bypassed. We present Contextual Integrity Verification (CIV), an inference-time security architecture that attaches cryptographically signed provenance labels to every token and enforces a source-trust lattice inside the transformer via a pre-softmax hard attention mask (with optional FFN/residual gating). CIV provides deterministic, per-token non-interference guarantees on frozen models: lower-trust tokens cannot influence higher-trust representations. On benchmarks derived from recent taxonomies of prompt-injection vectors (Elite-Attack + SoK-246), CIV attains 0% attack success rate under the stated threat model while preserving 93.1% token-level similarity and showing no degradation in model perplexity on benign tasks; we note a latency overhead attributable to a non-optimized data path. Because CIV is a lightweight patch -- no fine-tuning required -- we demonstrate drop-in protection for Llama-3-8B and Mistral-7B. We release a reference implementation, an automated certification harness, and the Elite-Attack corpus to support reproducible research.

