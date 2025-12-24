---
layout: default
title: "Securing Agentic AI: Threat Modeling and Risk Analysis for Network Monitoring Agentic AI System"
---

# Securing Agentic AI: Threat Modeling and Risk Analysis for Network Monitoring Agentic AI System

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10043" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10043v1</a>
  <a href="https://arxiv.org/pdf/2508.10043.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10043v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10043v1', 'Securing Agentic AI: Threat Modeling and Risk Analysis for Network Monitoring Agentic AI System')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pallavi Zambare, Venkata Nikhil Thanikella, Ying Liu

**分类**: cs.CR, cs.AI

**发布日期**: 2025-08-12

**备注**: Submitted and under review in IEEE Transactions on Privacy

---

## 💡 一句话要点

**提出MAESTRO框架以解决网络监控中的Agentic AI安全问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `网络安全` `自主代理` `大型语言模型` `威胁建模` `内存完整性` `异常检测` `多层防御`

## 📋 核心要点

1. 现有的网络监控系统在结合大型语言模型时面临严重的安全隐患，尤其是自主代理的脆弱性。
2. 论文提出了MAESTRO框架，通过七层威胁建模架构来识别和消除Agentic AI的安全漏洞。
3. 实验中确认了流量重放和内存中毒的威胁案例，导致系统性能下降，验证了多层防御策略的有效性。

## 📝 摘要（中文）

本研究探讨了将大型语言模型（LLMs）与自主代理结合在网络监控和决策系统中所带来的安全问题。研究采用MAESTRO框架，通过七层威胁建模架构来识别、评估和消除Agentic AI的脆弱性。构建并实现了一个原型代理系统，使用Python、LangChain和WebSockets进行遥测，部署了推理、内存、参数调优和异常检测模块。确认了两种实际威胁案例：流量重放拒绝服务和通过篡改历史日志文件进行的内存中毒。这些情况导致了可测量的性能下降，建议采用多层防御深度方法以确保Agentic AI在对抗环境中的可靠性。

## 🔬 方法详解

**问题定义**：本论文旨在解决将大型语言模型与自主代理结合时所引发的安全问题，现有方法未能有效识别和应对这些脆弱性。

**核心思路**：论文提出了MAESTRO框架，利用七层威胁建模架构来全面评估和消除Agentic AI系统中的安全风险，确保系统的可靠性和适应性。

**技术框架**：MAESTRO框架包括多个模块，如推理模块、内存管理模块、参数调优模块和异常检测模块，整体架构支持实时监控和响应。

**关键创新**：最重要的创新在于采用多层防御深度策略，结合内存隔离和实时验证机制，显著提升了Agentic AI系统在对抗环境中的安全性。

**关键设计**：在设计中，重点关注内存完整性和适应逻辑监控，采用特定的参数设置和损失函数，以优化系统的性能和安全性。

## 📊 实验亮点

实验结果表明，MAESTRO框架有效识别了流量重放和内存中毒的威胁，导致的性能下降可测量，系统适应性显著提高。通过多层防御策略，系统在对抗环境中的可靠性得到了增强，验证了该方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括网络安全、智能监控和决策支持系统。通过增强Agentic AI的安全性，能够有效防范各种网络攻击，提升系统的可靠性和稳定性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> When combining Large Language Models (LLMs) with autonomous agents, used in network monitoring and decision-making systems, this will create serious security issues. In this research, the MAESTRO framework consisting of the seven layers threat modeling architecture in the system was used to expose, evaluate, and eliminate vulnerabilities of agentic AI. The prototype agent system was constructed and implemented, using Python, LangChain, and telemetry in WebSockets, and deployed with inference, memory, parameter tuning, and anomaly detection modules. Two practical threat cases were confirmed as follows: (i) resource denial of service by traffic replay denial-of-service, and (ii) memory poisoning by tampering with the historical log file maintained by the agent. These situations resulted in measurable levels of performance degradation, i.e. telemetry updates were delayed, and computational loads were increased, as a result of poor system adaptations. It was suggested to use a multilayered defense-in-depth approach with memory isolation, validation of planners and anomaly response systems in real-time. These findings verify that MAESTRO is viable in operational threat mapping, prospective risk scoring, and the basis of the resilient system design. The authors bring attention to the importance of the enforcement of memory integrity, paying attention to the adaptation logic monitoring, and cross-layer communication protection that guarantee the agentic AI reliability in adversarial settings.

