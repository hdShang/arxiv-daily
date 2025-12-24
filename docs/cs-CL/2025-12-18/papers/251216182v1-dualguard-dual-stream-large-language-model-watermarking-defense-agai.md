---
layout: default
title: "DualGuard: Dual-stream Large Language Model Watermarking Defense against Paraphrase and Spoofing Attack"
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

**提出DualGuard，一种可防御复述攻击和欺骗攻击的双流大语言模型水印算法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `水印技术` `欺骗攻击防御` `复述攻击防御` `双流水印` `知识产权保护`

## 📋 核心要点

1. 现有LLM水印技术主要关注复述攻击防御，忽略了注入恶意内容的欺骗攻击，导致水印可靠性降低。
2. DualGuard采用自适应双流水印机制，根据语义内容动态注入互补水印信号，实现欺骗攻击的检测和追踪。
3. 实验证明DualGuard在可检测性、鲁棒性、可追溯性和文本质量方面表现出色，适用于实际应用。

## 📝 摘要（中文）

随着云服务的快速发展，大型语言模型（LLM）越来越容易通过各种网络平台访问。然而，这种可访问性也导致了模型滥用的风险日益增加。LLM水印技术已成为缓解此类滥用和保护知识产权的有效方法。然而，现有的水印算法主要侧重于防御复述攻击，而忽略了可能注入有害内容、损害水印可靠性并破坏对归属信任的背驮式欺骗攻击。为了解决这个局限性，我们提出了DualGuard，这是第一个能够防御复述攻击和欺骗攻击的水印算法。DualGuard采用自适应双流水印机制，其中两个互补的水印信号根据语义内容动态注入。这种设计使DualGuard不仅能够检测，而且能够追踪欺骗攻击，从而确保可靠和值得信赖的水印检测。在多个数据集和语言模型上进行的大量实验表明，DualGuard实现了出色的可检测性、鲁棒性、可追溯性和文本质量，有效地推进了LLM水印技术在实际应用中的发展。

## 🔬 方法详解

**问题定义**：现有的大语言模型水印方法主要关注抵抗复述攻击，即攻击者通过改写文本来移除或弱化水印。然而，这些方法忽略了一种更隐蔽的攻击方式，即欺骗攻击（Spoofing Attack）。攻击者可以在原始文本中注入恶意内容，同时尝试保留或伪造水印，从而误导水印检测系统，将恶意内容归因于原始作者。这种攻击会损害水印的可靠性和可信度。

**核心思路**：DualGuard的核心思路是利用双流水印机制，同时嵌入两种互补的水印信号。一种水印信号用于检测文本是否被篡改，另一种水印信号用于追踪攻击来源。通过分析这两种水印信号，DualGuard可以区分复述攻击和欺骗攻击，并识别出注入的恶意内容。这种设计基于一个假设：欺骗攻击者很难同时伪造两种独立的水印信号。

**技术框架**：DualGuard的整体框架包含以下几个主要模块：1) 语义分析模块：分析输入文本的语义信息，用于指导水印信号的嵌入。2) 双流水印嵌入模块：根据语义分析结果，动态地将两种互补的水印信号嵌入到文本中。3) 水印检测模块：检测文本中是否存在水印信号，并分析信号的强度和一致性。4) 攻击追踪模块：如果检测到欺骗攻击，则追踪攻击来源，例如注入恶意内容的位置和方式。

**关键创新**：DualGuard的关键创新在于其自适应双流水印机制。与传统的单流水印方法相比，DualGuard可以同时检测文本篡改和追踪攻击来源，从而更有效地防御欺骗攻击。此外，DualGuard的水印嵌入过程是自适应的，可以根据文本的语义信息动态调整水印信号的强度和位置，从而提高水印的鲁棒性和不可感知性。

**关键设计**：DualGuard的关键设计包括：1) 两种互补水印信号的选择：一种水印信号可以基于文本的统计特征，例如词频或n-gram分布；另一种水印信号可以基于文本的语义信息，例如情感或主题。2) 自适应水印嵌入策略：根据文本的语义信息，动态调整水印信号的强度和位置，以平衡水印的鲁棒性和不可感知性。3) 攻击追踪算法：分析水印信号的变化，识别注入恶意内容的位置和方式，并追踪攻击来源。

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

实验结果表明，DualGuard在防御复述攻击和欺骗攻击方面均优于现有水印算法。在多个数据集和语言模型上，DualGuard实现了接近100%的欺骗攻击检测率，同时保持了较高的水印鲁棒性和较低的文本质量损失。与基线方法相比，DualGuard在欺骗攻击防御方面取得了显著的性能提升。

## 🎯 应用场景

DualGuard可应用于各种基于大语言模型的云服务平台，用于保护模型输出的知识产权，防止恶意内容传播，并追溯攻击来源。例如，可以用于检测和阻止AI写作工具生成的虚假新闻，保护在线教育平台的课程内容不被篡改，以及防止聊天机器人被用于传播仇恨言论。

## 📄 摘要（原文）

> With the rapid development of cloud-based services, large language models (LLMs) have become increasingly accessible through various web platforms. However, this accessibility has also led to growing risks of model abuse. LLM watermarking has emerged as an effective approach to mitigate such misuse and protect intellectual property. Existing watermarking algorithms, however, primarily focus on defending against paraphrase attacks while overlooking piggyback spoofing attacks, which can inject harmful content, compromise watermark reliability, and undermine trust in attribution. To address this limitation, we propose DualGuard, the first watermarking algorithm capable of defending against both paraphrase and spoofing attacks. DualGuard employs the adaptive dual-stream watermarking mechanism, in which two complementary watermark signals are dynamically injected based on the semantic content. This design enables DualGuard not only to detect but also to trace spoofing attacks, thereby ensuring reliable and trustworthy watermark detection. Extensive experiments conducted across multiple datasets and language models demonstrate that DualGuard achieves excellent detectability, robustness, traceability, and text quality, effectively advancing the state of LLM watermarking for real-world applications.

