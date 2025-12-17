---
layout: default
title: Fighting AI with AI: Leveraging Foundation Models for Assuring AI-Enabled Safety-Critical Systems
---

# Fighting AI with AI: Leveraging Foundation Models for Assuring AI-Enabled Safety-Critical Systems

**arXiv**: [2511.20627v1](https://arxiv.org/abs/2511.20627) | [PDF](https://arxiv.org/pdf/2511.20627.pdf)

**作者**: Anastasia Mavridou, Divya Gopinath, Corina S. Păsăreanu

---

## 💡 一句话要点

**提出REACT和SemaLens以解决安全关键系统中AI组件的验证挑战**

**关键词**: `安全关键系统` `需求工程` `大型语言模型` `视觉语言模型` `深度神经网络验证`

## 📋 核心要点

1. AI组件在安全关键系统中引入不透明性和语义鸿沟，阻碍传统验证方法。
2. REACT使用LLM将自然语言需求转化为形式规范，支持早期验证。
3. SemaLens利用VLM测试和监控DNN感知系统，基于人类可理解概念。

## 📄 摘要（原文）

> The integration of AI components, particularly Deep Neural Networks (DNNs), into safety-critical systems such as aerospace and autonomous vehicles presents fundamental challenges for assurance. The opacity of AI systems, combined with the semantic gap between high-level requirements and low-level network representations, creates barriers to traditional verification approaches. These AI-specific challenges are amplified by longstanding issues in Requirements Engineering, including ambiguity in natural language specifications and scalability bottlenecks in formalization. We propose an approach that leverages AI itself to address these challenges through two complementary components. REACT (Requirements Engineering with AI for Consistency and Testing) employs Large Language Models (LLMs) to bridge the gap between informal natural language requirements and formal specifications, enabling early verification and validation. SemaLens (Semantic Analysis of Visual Perception using large Multi-modal models) utilizes Vision Language Models (VLMs) to reason about, test, and monitor DNN-based perception systems using human-understandable concepts. Together, these components provide a comprehensive pipeline from informal requirements to validated implementations.

