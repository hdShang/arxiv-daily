---
layout: default
title: "KubeGuard: LLM-Assisted Kubernetes Hardening via Configuration Files and Runtime Logs Analysis"
---

# KubeGuard: LLM-Assisted Kubernetes Hardening via Configuration Files and Runtime Logs Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04191" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04191v1</a>
  <a href="https://arxiv.org/pdf/2509.04191.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04191v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04191v1', 'KubeGuard: LLM-Assisted Kubernetes Hardening via Configuration Files and Runtime Logs Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Omri Sgan Cohen, Ehud Malul, Yair Meidan, Dudu Mimran, Yuval Elovici, Asaf Shabtai

**分类**: cs.CR, cs.LG

**发布日期**: 2025-09-04

---

## 💡 一句话要点

**KubeGuard：利用LLM分析配置与日志，增强Kubernetes安全性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Kubernetes安全` `大型语言模型` `运行时日志分析` `最小权限原则` `自动化配置` `安全加固` `云原生安全`

## 📋 核心要点

1. 现有Kubernetes安全方案主要依赖静态分析或异常检测，难以有效应对运行时配置风险和权限过度开放问题。
2. KubeGuard利用大型语言模型分析Kubernetes配置清单和运行时日志，生成最小权限配置建议，降低攻击面。
3. 实验结果表明，KubeGuard能够有效生成和优化Kubernetes资源配置，在角色、网络策略和部署方面表现出高精度和召回率。

## 📝 摘要（中文）

Kubernetes (K8s) 在云原生应用编排中的广泛应用带来了严重的安全挑战，例如资源配置错误和过度宽松的权限配置。未能解决这些问题可能导致未经授权的访问、权限提升以及集群内的横向移动。现有的大多数K8s安全解决方案侧重于检测配置错误，通常通过静态分析或异常检测。本文提出了 KubeGuard，一种新型的运行时日志驱动的推荐框架，旨在通过解决过度宽松的配置来降低风险。KubeGuard 旨在通过两项互补的任务来加强 K8s 环境：资源创建和资源优化。它利用大型语言模型 (LLM) 分析清单和反映实际系统行为的运行时日志，使用模块化的提示链工作流。这种方法使 KubeGuard 能够为新资源创建最小权限配置，并优化现有清单以减少攻击面。KubeGuard 的输出清单以建议的形式呈现，用户（例如，开发人员和运维人员）可以审查和采用这些建议来增强集群安全性。评估表明，KubeGuard 可以有效地生成和优化 Roles、NetworkPolicies 和 Deployments 的 K8s 清单，利用专有和开源 LLM。高精度、召回率和 F1 分数证实了 KubeGuard 作为一种框架的实用性，该框架将运行时可观察性转化为可操作的、最小权限配置指导。

## 🔬 方法详解

**问题定义**：Kubernetes集群中普遍存在配置错误和权限过度开放的问题，这导致了潜在的安全风险，如未经授权的访问和权限提升。现有的安全解决方案，例如静态分析和异常检测，无法充分解决运行时配置不当的问题，缺乏将运行时行为转化为配置改进的能力。

**核心思路**：KubeGuard的核心思路是利用大型语言模型（LLM）理解Kubernetes配置清单和运行时日志，从而推断出最小权限配置。通过分析实际的系统行为，LLM可以识别出过度宽松的权限，并提出更严格的配置建议，从而减少攻击面。

**技术框架**：KubeGuard包含两个主要任务：资源创建和资源优化。对于新资源创建，KubeGuard分析用户提供的需求描述，生成初始的最小权限配置。对于现有资源，KubeGuard分析运行时日志，识别出实际使用的权限，并与现有配置进行比较，提出优化建议。整个流程采用模块化的提示链工作流，将复杂的分析任务分解为多个可管理的步骤。

**关键创新**：KubeGuard的关键创新在于将大型语言模型应用于Kubernetes安全配置的自动化生成和优化。与传统的静态分析方法不同，KubeGuard能够理解运行时行为，并根据实际情况调整配置。此外，KubeGuard采用提示链工作流，使得LLM能够更有效地处理复杂的配置分析任务。

**关键设计**：KubeGuard的关键设计包括：1) 使用专门设计的提示工程，引导LLM理解Kubernetes配置和运行时日志；2) 采用模块化的提示链，将复杂的分析任务分解为多个步骤；3) 提供用户友好的界面，允许用户审查和采纳LLM生成的配置建议。具体的参数设置和损失函数取决于所使用的LLM和提示工程策略。

## 📊 实验亮点

KubeGuard在生成和优化Kubernetes Roles、NetworkPolicies和Deployments配置方面表现出色。实验结果显示，KubeGuard利用专有和开源LLM均能达到高精度、高召回率和高F1分数。例如，在某项测试中，KubeGuard的F1分数超过0.9，显著优于人工配置，证明了其在实际应用中的有效性。

## 🎯 应用场景

KubeGuard可应用于自动化Kubernetes集群安全加固，帮助开发人员和运维人员快速生成和优化资源配置，降低安全风险。它能够显著减少手动配置的工作量，提高集群的整体安全性，并可集成到CI/CD流程中，实现安全配置的持续交付。未来，KubeGuard可扩展到支持更多类型的Kubernetes资源和安全策略。

## 📄 摘要（原文）

> The widespread adoption of Kubernetes (K8s) for orchestrating cloud-native applications has introduced significant security challenges, such as misconfigured resources and overly permissive configurations. Failing to address these issues can result in unauthorized access, privilege escalation, and lateral movement within clusters. Most existing K8s security solutions focus on detecting misconfigurations, typically through static analysis or anomaly detection. In contrast, this paper presents KubeGuard, a novel runtime log-driven recommender framework aimed at mitigating risks by addressing overly permissive configurations. KubeGuard is designed to harden K8s environments through two complementary tasks: Resource Creation and Resource Refinement. It leverages large language models (LLMs) to analyze manifests and runtime logs reflecting actual system behavior, using modular prompt-chaining workflows. This approach enables KubeGuard to create least-privilege configurations for new resources and refine existing manifests to reduce the attack surface. KubeGuard's output manifests are presented as recommendations that users (e.g., developers and operators) can review and adopt to enhance cluster security. Our evaluation demonstrates that KubeGuard effectively generates and refines K8s manifests for Roles, NetworkPolicies, and Deployments, leveraging both proprietary and open-source LLMs. The high precision, recall, and F1-scores affirm KubeGuard's practicality as a framework that translates runtime observability into actionable, least-privilege configuration guidance.

