---
layout: default
title: REMSA: An LLM Agent for Foundation Model Selection in Remote Sensing
---

# REMSA: An LLM Agent for Foundation Model Selection in Remote Sensing

**arXiv**: [2511.17442v1](https://arxiv.org/abs/2511.17442) | [PDF](https://arxiv.org/pdf/2511.17442.pdf)

**作者**: Binger Chen, Tacettin Emre Bök, Behnood Rasti, Volker Markl, Begüm Demir

---

## 💡 一句话要点

**提出REMSA LLM代理以解决遥感基础模型选择难题**

**关键词**: `遥感基础模型` `模型选择代理` `LLM应用` `多模态数据` `自然语言查询` `基准评估`

## 📋 核心要点

1. 遥感基础模型选择困难，文档分散、格式异构、部署约束多样
2. 构建RS-FMD数据库，开发REMSA代理，通过自然语言查询自动选择模型
3. 在专家验证基准上，REMSA优于基线方法，提供透明解释

## 📄 摘要（原文）

> Foundation Models (FMs) are increasingly used in remote sensing (RS) for tasks such as environmental monitoring, disaster assessment, and land-use mapping. These models include unimodal vision encoders trained on a single data modality and multimodal architectures trained on combinations of SAR, multispectral, hyperspectral, and image-text data. They support diverse RS tasks including semantic segmentation, image classification, change detection, and visual question answering. However, selecting an appropriate remote sensing foundation model (RSFM) remains difficult due to scattered documentation, heterogeneous formats, and varied deployment constraints. We introduce the RSFM Database (RS-FMD), a structured resource covering over 150 RSFMs spanning multiple data modalities, resolutions, and learning paradigms. Built on RS-FMD, we present REMSA, the first LLM-based agent for automated RSFM selection from natural language queries. REMSA interprets user requirements, resolves missing constraints, ranks candidate models using in-context learning, and provides transparent justifications. We also propose a benchmark of 75 expert-verified RS query scenarios, producing 900 configurations under an expert-centered evaluation protocol. REMSA outperforms several baselines, including naive agents, dense retrieval, and unstructured RAG-based LLMs. It operates entirely on publicly available metadata and does not access private or sensitive data.

