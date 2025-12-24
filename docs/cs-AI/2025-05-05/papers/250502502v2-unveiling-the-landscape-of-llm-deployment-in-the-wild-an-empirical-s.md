---
layout: default
title: "Unveiling the Landscape of LLM Deployment in the Wild: An Empirical Study"
---

# Unveiling the Landscape of LLM Deployment in the Wild: An Empirical Study

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02502" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02502v2</a>
  <a href="https://arxiv.org/pdf/2505.02502.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02502v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02502v2', 'Unveiling the Landscape of LLM Deployment in the Wild: An Empirical Study')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinyi Hou, Jiahao Han, Yanjie Zhao, Haoyu Wang

**分类**: cs.CR, cs.AI, cs.SE

**发布日期**: 2025-05-05 (更新: 2025-08-26)

---

## 💡 一句话要点

**揭示LLM部署中的安全风险与改进措施**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `安全性` `API端点` `TLS配置` `公共服务` `系统脆弱性` `部署实践`

## 📋 核心要点

1. 现有LLM部署面临安全性和可靠性问题，尤其是错误配置和不安全的默认设置使服务暴露于公共互联网。
2. 通过对公共LLM服务的实证研究，论文识别了320,102个服务及其安全风险，提出了改进部署实践的必要性。
3. 研究发现，超过40%的API端点使用不安全的HTTP协议，强调了对安全协议和认证机制的需求。

## 📝 摘要（中文）

大型语言模型（LLMs）通过开源和商业框架的广泛部署，使个人和组织能够自托管先进的LLM能力。然而，安全性和可靠性的保障成为关键问题。本研究对公共LLM服务的部署进行了大规模实证调查，发现超过40%的API端点使用明文HTTP，且超过21万个端点缺乏有效的TLS元数据，暴露出严重的安全风险。这些风险包括模型泄露、系统妥协和未授权访问，强调了需要安全默认设置和更强的部署实践。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型（LLM）在公共互联网部署中的安全性问题，现有方法常因不安全的默认设置和错误配置而导致服务暴露，增加了安全风险。

**核心思路**：通过大规模的互联网测量，识别和分析公共LLM服务的部署情况，评估其安全性和系统性脆弱性，以提出改进建议。

**技术框架**：研究采用了互联网范围的测量方法，分析了15种框架下的320,102个公共LLM服务，提取了158个独特的API端点，并根据功能和安全风险将其分类为12个功能组。

**关键创新**：本研究的创新点在于系统性地评估了公共LLM服务的安全性，揭示了API暴露的不一致性和广泛使用的不安全协议，强调了安全默认设置的重要性。

**关键设计**：研究中对API端点的安全性进行了详细分析，发现超过40%的端点使用明文HTTP，且210,000多个端点缺乏有效的TLS元数据，部分框架如Ollama对未认证请求的响应率超过35%。

## 📊 实验亮点

研究发现，超过40%的API端点使用明文HTTP，且210,000多个端点缺乏有效的TLS元数据，部分框架对未认证请求的响应率超过35%。这些结果突显了当前LLM服务在安全性方面的严重不足，亟需改进。

## 🎯 应用场景

该研究的结果对企业和开发者在部署LLM时具有重要指导意义，能够帮助他们识别和修复潜在的安全漏洞，从而提高服务的安全性和可靠性。未来，研究成果可推动更安全的LLM部署实践和框架的设计。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly deployed through open-source and commercial frameworks, enabling individuals and organizations to self-host advanced LLM capabilities. As LLM deployments become prevalent, particularly in industry, ensuring their secure and reliable operation has become a critical issue. However, insecure defaults and misconfigurations often expose LLM services to the public internet, posing serious security and system engineering risks. This study conducted a large-scale empirical investigation of public-facing LLM deployments, focusing on the prevalence of services, exposure characteristics, systemic vulnerabilities, and associated risks. Through internet-wide measurements, we identified 320,102 public-facing LLM services across 15 frameworks and extracted 158 unique API endpoints, categorized into 12 functional groups based on functionality and security risk. Our analysis found that over 40% of endpoints used plain HTTP, and over 210,000 endpoints lacked valid TLS metadata. API exposure was highly inconsistent: some frameworks, such as Ollama, responded to over 35% of unauthenticated API requests, with about 15% leaking model or system information, while other frameworks implemented stricter controls. We observed widespread use of insecure protocols, poor TLS configurations, and unauthenticated access to critical operations. These security risks, such as model leakage, system compromise, and unauthorized access, are pervasive and highlight the need for a secure-by-default framework and stronger deployment practices.

