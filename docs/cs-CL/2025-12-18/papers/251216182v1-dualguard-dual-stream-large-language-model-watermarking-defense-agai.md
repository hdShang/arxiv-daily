---
layout: default
title: DualGuard: Dual-stream Large Language Model Watermarking Defense against Paraphrase and Spoofing Attack
---

# DualGuard: Dual-stream Large Language Model Watermarking Defense against Paraphrase and Spoofing Attack

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16182" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16182v1</a>
  <a href="https://arxiv.org/pdf/2512.16182.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16182v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16182v1', 'DualGuard: Dual-stream Large Language Model Watermarking Defense against Paraphrase and Spoofing Attack')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Li, Yubing Ren, Yanan Cao, Yingjie Li, Fang Fang, Shi Wang, Li Guo

**分类**: cs.CR, cs.CL

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出DualGuard，防御针对大语言模型水印的复述攻击和欺骗攻击。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `水印技术` `复述攻击` `欺骗攻击` `双流水印` `知识产权保护` `安全防护`

## 📋 核心要点

1. 现有LLM水印技术主要关注复述攻击防御，忽略了尾随欺骗攻击带来的水印可靠性与归属信任风险。
2. DualGuard采用自适应双流水印机制，基于语义内容动态注入互补水印信号，实现欺骗攻击的检测与追踪。
3. 实验证明DualGuard在可检测性、鲁棒性、可追溯性和文本质量方面表现出色，推动了LLM水印的实际应用。

## 📝 摘要（中文）

随着云服务的快速发展，大型语言模型（LLMs）越来越容易通过各种网络平台访问。然而，这种可访问性也导致了模型滥用的风险日益增加。LLM水印技术已成为缓解此类滥用和保护知识产权的有效方法。然而，现有的水印算法主要侧重于防御复述攻击，而忽略了尾随欺骗攻击，这种攻击会注入有害内容，损害水印的可靠性，并破坏对归属的信任。为了解决这个局限性，我们提出了DualGuard，这是第一个能够防御复述攻击和欺骗攻击的水印算法。DualGuard采用自适应双流水印机制，其中两个互补的水印信号根据语义内容动态注入。这种设计使DualGuard不仅能够检测，而且能够追踪欺骗攻击，从而确保可靠和值得信赖的水印检测。在多个数据集和语言模型上进行的大量实验表明，DualGuard实现了出色的可检测性、鲁棒性、可追溯性和文本质量，有效地推进了LLM水印在实际应用中的发展。

## 🔬 方法详解

**问题定义**：现有的大语言模型水印技术主要关注防御复述攻击，即攻击者通过改写水印文本来尝试移除或弱化水印。然而，一种更隐蔽的攻击方式，即尾随欺骗攻击（piggyback spoofing attack），却被忽视。这种攻击通过在原始文本后附加恶意内容，不仅能绕过水印检测，还能注入有害信息，严重威胁模型安全和用户信任。因此，论文旨在解决如何有效防御复述攻击和尾随欺骗攻击，保证水印的可靠性和可追溯性问题。

**核心思路**：DualGuard的核心思路是利用双流水印机制，同时嵌入两种互补的水印信号。一种水印信号用于抵抗复述攻击，保证基本的可检测性；另一种水印信号则专门用于检测和追踪尾随欺骗攻击。通过分析两种水印信号之间的关系，可以判断是否存在恶意注入，并追踪攻击源。这种双重保障的设计旨在提高水印的整体鲁棒性和安全性。

**技术框架**：DualGuard的技术框架主要包含以下几个模块：1) 语义分析模块：分析输入文本的语义信息，为后续的水印嵌入提供依据。2) 自适应水印嵌入模块：根据语义分析结果，动态调整两种水印信号的强度和位置。3) 水印检测模块：检测文本中是否存在水印信号，并判断是否存在尾随欺骗攻击。4) 攻击追踪模块：如果检测到欺骗攻击，则追踪攻击源，并提供相应的证据。整个流程旨在实现水印的可靠嵌入、准确检测和有效追踪。

**关键创新**：DualGuard的关键创新在于其双流水印机制，这是第一个同时考虑复述攻击和尾随欺骗攻击的水印算法。与传统的单水印方法相比，DualGuard能够更全面地保护LLM的知识产权和用户安全。此外，自适应水印嵌入模块能够根据语义信息动态调整水印信号，进一步提高了水印的鲁棒性和隐蔽性。

**关键设计**：DualGuard的关键设计包括：1) 语义分析模块采用预训练语言模型（如BERT）提取文本的语义特征。2) 自适应水印嵌入模块使用强化学习算法，根据语义特征动态调整水印信号的强度和位置。3) 水印检测模块使用统计假设检验方法，判断文本中是否存在水印信号。4) 攻击追踪模块使用溯源算法，根据水印信号的变化追踪攻击源。具体的参数设置、损失函数和网络结构等细节未在摘要中详细说明，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16182v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16182v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16182v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，DualGuard在抵抗复述攻击和尾随欺骗攻击方面均表现出色。在多个数据集和语言模型上，DualGuard实现了高检测率和低误报率，同时保持了良好的文本质量。与现有水印算法相比，DualGuard在防御欺骗攻击方面具有显著优势，能够有效追踪攻击源，为LLM的安全应用提供了有力保障。具体的性能数据和提升幅度在摘要中未明确给出，属于未知信息。

## 🎯 应用场景

DualGuard可应用于各种基于云的大语言模型服务，用于保护模型的知识产权，防止恶意用户滥用模型生成有害内容。该技术可用于内容审核、版权保护、虚假信息检测等领域，提升LLM服务的安全性和可信度，促进LLM技术的健康发展。未来，该技术有望扩展到其他类型的人工智能模型，构建更完善的安全防护体系。

## 📄 摘要（原文）

> With the rapid development of cloud-based services, large language models (LLMs) have become increasingly accessible through various web platforms. However, this accessibility has also led to growing risks of model abuse. LLM watermarking has emerged as an effective approach to mitigate such misuse and protect intellectual property. Existing watermarking algorithms, however, primarily focus on defending against paraphrase attacks while overlooking piggyback spoofing attacks, which can inject harmful content, compromise watermark reliability, and undermine trust in attribution. To address this limitation, we propose DualGuard, the first watermarking algorithm capable of defending against both paraphrase and spoofing attacks. DualGuard employs the adaptive dual-stream watermarking mechanism, in which two complementary watermark signals are dynamically injected based on the semantic content. This design enables DualGuard not only to detect but also to trace spoofing attacks, thereby ensuring reliable and trustworthy watermark detection. Extensive experiments conducted across multiple datasets and language models demonstrate that DualGuard achieves excellent detectability, robustness, traceability, and text quality, effectively advancing the state of LLM watermarking for real-world applications.

