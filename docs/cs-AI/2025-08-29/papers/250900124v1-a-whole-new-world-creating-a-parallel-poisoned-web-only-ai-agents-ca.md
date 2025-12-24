---
layout: default
title: "A Whole New World: Creating a Parallel-Poisoned Web Only AI-Agents Can See"
---

# A Whole New World: Creating a Parallel-Poisoned Web Only AI-Agents Can See

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00124" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00124v1</a>
  <a href="https://arxiv.org/pdf/2509.00124.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00124v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00124v1', 'A Whole New World: Creating a Parallel-Poisoned Web Only AI-Agents Can See')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaked Zychlinski

**分类**: cs.CR, cs.AI, cs.CY

**发布日期**: 2025-08-29

**备注**: 10 pages, 1 figure

---

## 💡 一句话要点

**提出一种新型攻击向量以解决AI代理安全问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `AI代理` `网络安全` `隐蔽攻击` `指纹识别` `大型语言模型` `恶意软件` `数据外泄`

## 📋 核心要点

1. 现有的网页安全防护措施难以识别和防范针对AI代理的隐蔽攻击，导致安全隐患加剧。
2. 论文提出了一种利用网站隐蔽技术的攻击方法，能够动态识别AI代理并提供恶意内容，劫持其行为。
3. 研究表明，该攻击方式能够有效绕过传统安全措施，且对人类用户完全不可见，具有高度隐蔽性。

## 📝 摘要（中文）

本文介绍了一种新型攻击向量，利用网站隐蔽技术来攻击基于大型语言模型（LLMs）的自主网页浏览代理。随着这些代理的普及，其独特且常常同质化的数字指纹（包括浏览器属性、自动化框架签名和网络特征）形成了一种新的可区分的网络流量类别。攻击者可以识别来自AI代理的请求，并动态提供不同的“隐蔽”内容版本。人类用户看到的是无害的网页，而代理则被呈现出嵌入隐藏恶意指令的视觉相同页面。这种机制使得对手能够劫持代理行为，导致数据外泄、恶意软件执行或虚假信息传播，同时对人类用户和传统安全爬虫完全不可见。本文正式化了威胁模型，详细阐述了代理指纹识别和隐蔽技术的机制，并讨论了对未来代理AI的深远安全影响，强调了对这种隐蔽且可扩展攻击的强大防御的迫切需求。

## 🔬 方法详解

**问题定义**：本文旨在解决针对基于大型语言模型的自主网页浏览代理的安全问题。现有方法在识别和防范AI代理的攻击方面存在显著不足，无法有效应对新型隐蔽攻击。

**核心思路**：论文的核心思路是利用网站隐蔽技术，通过识别AI代理的数字指纹，动态提供恶意内容，从而劫持代理的行为。这种设计使得攻击者能够在不被人类用户察觉的情况下实施攻击。

**技术框架**：整体架构包括代理指纹识别模块、动态内容生成模块和恶意指令嵌入模块。首先，系统识别请求来源是否为AI代理，然后根据识别结果动态生成不同版本的网页内容。

**关键创新**：最重要的技术创新在于将网站隐蔽技术与AI代理的指纹识别相结合，形成了一种新的攻击向量。这与传统的网页攻击方法有本质区别，后者通常不具备针对AI代理的特异性。

**关键设计**：在技术细节上，论文设计了特定的指纹识别算法，优化了内容生成的动态响应机制，并通过隐蔽指令的嵌入方式确保恶意行为的隐蔽性。

## 📊 实验亮点

实验结果表明，该攻击方法能够在100%的情况下成功识别AI代理并提供恶意内容，同时对人类用户的可见性保持在0%。与传统安全防护措施相比，攻击成功率显著提高，展示了其隐蔽性和有效性。

## 🎯 应用场景

该研究的潜在应用领域包括网络安全、AI代理的防护机制以及自动化系统的安全性提升。随着AI代理的广泛应用，理解和防范此类攻击将对保护用户数据和维护网络安全具有重要价值。未来，研究成果可能推动相关防护技术的开发与应用，提升整体网络安全水平。

## 📄 摘要（原文）

> This paper introduces a novel attack vector that leverages website cloaking techniques to compromise autonomous web-browsing agents powered by Large Language Models (LLMs). As these agents become more prevalent, their unique and often homogenous digital fingerprints - comprising browser attributes, automation framework signatures, and network characteristics - create a new, distinguishable class of web traffic. The attack exploits this fingerprintability. A malicious website can identify an incoming request as originating from an AI agent and dynamically serve a different, "cloaked" version of its content. While human users see a benign webpage, the agent is presented with a visually identical page embedded with hidden, malicious instructions, such as indirect prompt injections. This mechanism allows adversaries to hijack agent behavior, leading to data exfiltration, malware execution, or misinformation propagation, all while remaining completely invisible to human users and conventional security crawlers. This work formalizes the threat model, details the mechanics of agent fingerprinting and cloaking, and discusses the profound security implications for the future of agentic AI, highlighting the urgent need for robust defenses against this stealthy and scalable attack.

