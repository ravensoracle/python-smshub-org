# -*- coding: utf-8 -*-
import inspect


class ErrorsModel(Exception):
	def __init__(self):
		super().__init__(self.message, self.code)


class ServiceModel:
	@property
	def short_name(self):
		return self.__service_short_name

	@property
	def count(self):
		return self.__count_slot

	@count.setter
	def count(self, value):
		self.__count_slot = int(value)

	@property
	def priceMap(self):
		return self.__service_price_map

	@priceMap.setter
	def priceMap(self, dict_map):
		self.__service_price_map = dict_map

	@property
	def prices(self):
		return self.__service_prices

	@prices.setter
	def prices(self, prices_list):
		self.__service_prices = prices_list

	@property
	def quantities(self):
		return self.__service_quantities

	@quantities.setter
	def quantities(self, quantities_list):
		self.__service_quantities = quantities_list

	@property
	def minPrice(self):
		return self.__service_min_price

	@minPrice.setter
	def minPrice(self, value):
		if type(value) == tuple:
			self.__service_min_price = (float(value[0]), int(value[1]))
		else:
			self.__service_min_price = value

	@property
	def maxPrice(self, value):
		if type(value) == tuple:
			self.__service_max_price = (float(value[0]), int(value[1]))
		else:
			self.__service_max_price = value

	@maxPrice.setter
	def maxPrice(self, value):
		if len(value) == 2:
			self.__service_max_price = (float(value[0]), int(value[1]))
		else:
			self.__service_max_price = value

	@property
	def work(self):
		return self.__service_is_work

	@work.setter
	def work(self, value):
		self.__service_is_work = bool(value)


class ActionsModel:
	__action_name = ''
	__response_data = ''

	def __init__(self, current):
		self.__request_data = {'action': self._name}
		self.data = self._build(current)

	def _build(self, frame):
		args, _, _, values = inspect.getargvalues(frame)
		exclude = ['self', 'callback', 'wrapper']
		result = {}
		for i in args:
			if i == 'ref':
				values[i] = 'python' + __name__.split('.')[0][:-2]
			elif not values[i]:
				continue
			if i in exclude:
				continue
			result[i] = values[i]
		return result

	@property
	def data(self):
		return self.__request_data

	@data.setter
	def data(self, value):
		self.__request_data = {**self.__request_data, **value}

	@property
	def _name(self):
		return self.__action_name

	@_name.setter
	def _name(self, value):
		self.__action_name = value