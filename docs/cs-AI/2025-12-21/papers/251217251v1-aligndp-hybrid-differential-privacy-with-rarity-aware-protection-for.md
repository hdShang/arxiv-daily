---
layout: default
title: "AlignDP: Hybrid Differential Privacy with Rarity-Aware Protection for LLMs"
---

# AlignDP: Hybrid Differential Privacy with Rarity-Aware Protection for LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17251" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17251v1</a>
  <a href="https://arxiv.org/pdf/2512.17251.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17251v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17251v1', 'AlignDP: Hybrid Differential Privacy with Rarity-Aware Protection for LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Madhava Gaikwad

**分类**: cs.CR, cs.AI, cs.LG

**发布日期**: 2025-12-19

**备注**: 39th Conference on Neural Information Processing Systems (NeurIPS 2025) Workshop: LOCK-LLM Work-shop, NeurIPS 2025

---

## 💡 一句话要点

**AlignDP：针对LLM的混合差分隐私方法，通过稀有感知保护提升安全性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `差分隐私` `大型语言模型` `隐私保护` `PAC学习` `RAPPOR`

## 📋 核心要点

1. 大型语言模型面临数据泄露风险，现有防御方法通常在泄露后才生效，缺乏主动防御能力。
2. AlignDP提出一种混合差分隐私方法，区分稀有和非稀有字段，分别采用PAC不可区分性和RAPPOR进行保护。
3. 实验结果表明，AlignDP能够在隐藏稀有类别的同时，以较小的误差恢复频繁类别，验证了其可行性。

## 📝 摘要（中文）

大型语言模型面临提取、蒸馏和未经授权的微调等风险。现有的防御措施如水印或监控，都是在泄露发生后才起作用。本文设计了AlignDP，一种混合隐私锁，可在数据接口处阻止知识转移。核心思想是将稀有字段和非稀有字段分离。稀有字段通过PAC不可区分性进行保护，实现有效的零epsilon局部差分隐私（DP）。非稀有字段使用RAPPOR进行私有化，从而在局部DP下提供无偏的频率估计。全局聚合器强制执行组合和预算。这种双层设计隐藏了稀有事件，并为频繁事件添加了可控噪声。论文证明了PAC扩展到全局聚合的限制，给出了RAPPOR估计的界限，并分析了效用权衡。玩具仿真实验证实了可行性：稀有类别保持隐藏，频繁类别以小误差恢复。

## 🔬 方法详解

**问题定义**：大型语言模型容易受到各种攻击，包括数据提取、模型蒸馏和未经授权的微调。现有的防御机制，例如水印和监控系统，通常是在数据泄露发生后才采取行动，缺乏主动预防措施。因此，需要一种在数据层面主动阻止知识转移的隐私保护机制。

**核心思路**：AlignDP的核心思想是根据数据字段的稀有程度采用不同的差分隐私策略。对于稀有字段，采用PAC（Probably Approximately Correct）不可区分性，提供更强的隐私保护，近似于零epsilon的局部差分隐私。对于非稀有字段，采用RAPPOR（Randomized Aggregatable Privacy-Preserving Ordinal Response），在局部差分隐私下提供无偏的频率估计。

**技术框架**：AlignDP包含以下主要模块：1) 数据字段分类器：区分稀有和非稀有字段。2) 稀有字段保护模块：应用PAC不可区分性。3) 非稀有字段保护模块：使用RAPPOR进行私有化。4) 全局聚合器：汇总来自不同用户的私有化数据，并强制执行差分隐私预算。整体流程是，用户首先对数据进行分类，然后根据字段类型应用相应的隐私保护机制，最后将私有化后的数据发送到全局聚合器进行分析。

**关键创新**：AlignDP的关键创新在于其混合差分隐私策略，它根据数据字段的稀有程度自适应地调整隐私保护强度。这种方法能够在保护稀有数据的同时，保持对频繁数据的分析效用。此外，论文还分析了PAC扩展到全局聚合的限制，并给出了RAPPOR估计的界限。

**关键设计**：AlignDP的关键设计包括：1) 稀有字段的PAC不可区分性实现方式，具体如何选择合适的PAC参数以达到所需的隐私级别。2) RAPPOR的参数设置，例如哈希函数的数量和扰动概率，这些参数会影响隐私保护强度和数据效用之间的权衡。3) 全局聚合器的设计，如何有效地汇总来自不同用户的私有化数据，并控制差分隐私预算。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17251v1/aligndp_pipeline.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17251v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17251v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文通过玩具仿真实验验证了AlignDP的可行性。实验结果表明，AlignDP能够在隐藏稀有类别的同时，以较小的误差恢复频繁类别。这表明AlignDP能够在隐私保护和数据效用之间取得良好的平衡。具体的性能数据和对比基线未知，需要在论文中查找。

## 🎯 应用场景

AlignDP可应用于各种需要保护用户数据隐私的大型语言模型应用场景，例如医疗健康、金融服务和法律咨询等。通过在数据接口处阻止知识转移，AlignDP可以有效防止敏感信息的泄露，提高用户对LLM的信任度，并促进LLM在隐私敏感领域的应用。

## 📄 摘要（原文）

> Large language models are exposed to risks of extraction, distillation, and unauthorized fine-tuning. Existing defenses use watermarking or monitoring, but these act after leakage. We design AlignDP, a hybrid privacy lock that blocks knowledge transfer at the data interface. The key idea is to separate rare and non-rare fields. Rare fields are shielded by PAC indistinguishability, giving effective zero-epsilon local DP. Non-rare fields are privatized with RAPPOR, giving unbiased frequency estimates under local DP. A global aggregator enforces composition and budget. This two-tier design hides rare events and adds controlled noise to frequent events. We prove limits of PAC extension to global aggregation, give bounds for RAPPOR estimates, and analyze utility trade-off. A toy simulation confirms feasibility: rare categories remain hidden, frequent categories are recovered with small error.

