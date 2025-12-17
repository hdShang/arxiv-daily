---
layout: default
title: Verifying rich robustness properties for neural networks
---

# Verifying rich robustness properties for neural networks

**arXiv**: [2511.07293v1](https://arxiv.org/abs/2511.07293) | [PDF](https://arxiv.org/pdf/2511.07293.pdf)

**作者**: Mohammad Afzal, S. Akshay, Ashutosh Gupta

---

## 💡 一句话要点

**提出统一框架以验证神经网络鲁棒性变体，支持置信度考量。**

**关键词**: `神经网络验证` `鲁棒性规范` `置信度考量` `统一验证框架` `近似误差控制`

## 📋 核心要点

1. 核心问题：现有方法忽略神经网络输出置信度，且编码复杂，难以验证多种鲁棒性变体。
2. 方法要点：使用简单语法定义规范，通过添加层统一验证，兼容现有工具并控制近似误差。
3. 实验或效果：在8870个基准测试中验证，涵盖138M参数网络，性能优于直接编码方法。

## 📄 摘要（原文）

> Robustness is a important problem in AI alignment and safety, with models
> such as neural networks being increasingly used in safety-critical systems. In
> the last decade, a large body of work has emerged on local robustness, i.e.,
> checking if the decision of a neural network remains unchanged when the input
> is slightly perturbed. However, many of these approaches require specialized
> encoding and often ignore the confidence of a neural network on its output. In
> this paper, our goal is to build a generalized framework to specify and verify
> variants of robustness in neural network verification. We propose a
> specification framework using a simple grammar, which is flexible enough to
> capture most existing variants. This allows us to introduce new variants of
> robustness that take into account the confidence of the neural network in its
> outputs. Next, we develop a novel and powerful unified technique to verify all
> such variants in a homogeneous way, viz., by adding a few additional layers to
> the neural network. This enables us to use any state-of-the-art neural network
> verification tool, without having to tinker with the encoding within, while
> incurring an approximation error that we show is bounded. We perform an
> extensive experimental evaluation over a large suite of 8870 benchmarks having
> 138M parameters in a largest network, and show that we are able to capture a
> wide set of robustness variants and outperform direct encoding approaches by a
> significant margin.

